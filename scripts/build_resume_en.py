from pathlib import Path
import re
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'resumes' / 'resume-en-current.md'
BUILD = ROOT / '.build'
BUILD.mkdir(exist_ok=True)
OUT = BUILD / 'resume-en-current.docx'


def clean_bold(s: str) -> str:
    s = s.strip()
    if s.startswith('**') and s.endswith('**'):
        return s[2:-2]
    return s


def parse_source(path: Path):
    lines = path.read_text(encoding='utf-8').splitlines()
    nonempty = [i for i, line in enumerate(lines) if line.strip()]
    name = lines[nonempty[0]].strip()[2:].strip()
    title = clean_bold(lines[nonempty[1]])
    contact = lines[nonempty[2]].strip()
    sections = []
    current = None
    for raw in lines[nonempty[2] + 1:]:
        line = raw.strip()
        if not line:
            continue
        if line.startswith('## '):
            current = {'name': line[3:].strip(), 'items': []}
            sections.append(current)
        elif current is not None:
            current['items'].append(line)
    return name, title, contact, sections


def add_bottom_border(paragraph, color='B7B7B7', size='6'):
    p_pr = paragraph._p.get_or_add_pPr()
    p_bdr = p_pr.find(qn('w:pBdr'))
    if p_bdr is None:
        p_bdr = OxmlElement('w:pBdr')
        p_pr.append(p_bdr)
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), size)
    bottom.set(qn('w:space'), '2')
    bottom.set(qn('w:color'), color)
    p_bdr.append(bottom)


def build_docx(name, title, contact, sections, out_path: Path):
    doc = Document()
    sec = doc.sections[0]
    sec.top_margin = Inches(0.42)
    sec.bottom_margin = Inches(0.42)
    sec.left_margin = Inches(0.58)
    sec.right_margin = Inches(0.58)

    styles = doc.styles
    normal = styles['Normal']
    normal.font.name = 'Arial'
    normal._element.rPr.rFonts.set(qn('w:eastAsia'), 'Arial')
    normal.font.size = Pt(9.35)
    normal.paragraph_format.space_after = Pt(0)
    normal.paragraph_format.line_spacing = 1.0

    for style_name, size, bold, italic in [
        ('ResumeSection', 10.2, True, False),
        ('ResumeEntry', 9.75, True, False),
        ('ResumeMeta', 8.7, False, False),
        ('ResumeTech', 8.65, False, True),
        ('ResumeBullet', 9.15, False, False),
    ]:
        style = styles[style_name] if style_name in styles else styles.add_style(style_name, WD_STYLE_TYPE.PARAGRAPH)
        style.font.name = 'Arial'
        style._element.rPr.rFonts.set(qn('w:eastAsia'), 'Arial')
        style.font.size = Pt(size)
        style.font.bold = bold
        style.font.italic = italic
        style.paragraph_format.space_after = Pt(0)
        style.paragraph_format.line_spacing = 1.0

    def add_section(text):
        paragraph = doc.add_paragraph(style='ResumeSection')
        paragraph.paragraph_format.space_before = Pt(4.2)
        paragraph.paragraph_format.space_after = Pt(2.2)
        paragraph.add_run(text.upper()).bold = True
        add_bottom_border(paragraph)
        return paragraph

    def add_entry(text, date=None):
        paragraph = doc.add_paragraph(style='ResumeEntry')
        paragraph.paragraph_format.space_before = Pt(1.2)
        paragraph.paragraph_format.space_after = Pt(0.5)
        if date:
            paragraph.paragraph_format.tab_stops.add_tab_stop(
                Inches(7.08), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.SPACES
            )
            paragraph.add_run(text).bold = True
            paragraph.add_run('\t' + date).bold = True
        else:
            paragraph.add_run(text).bold = True
        return paragraph

    def add_tech(text):
        paragraph = doc.add_paragraph(style='ResumeTech')
        paragraph.paragraph_format.space_after = Pt(0.6)
        run = paragraph.add_run(text)
        run.italic = True
        run.font.color.rgb = RGBColor(70, 70, 70)
        return paragraph

    def add_bullet(text):
        paragraph = doc.add_paragraph(style='ResumeBullet')
        paragraph.paragraph_format.left_indent = Inches(0.15)
        paragraph.paragraph_format.first_line_indent = Inches(-0.11)
        paragraph.paragraph_format.space_after = Pt(0.7)
        paragraph.add_run('• ')
        paragraph.add_run(text)
        return paragraph

    paragraph = doc.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.paragraph_format.space_after = Pt(0)
    run = paragraph.add_run(name.upper())
    run.bold = True
    run.font.size = Pt(17.5)

    paragraph = doc.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.paragraph_format.space_after = Pt(1.0)
    run = paragraph.add_run(title)
    run.bold = True
    run.font.size = Pt(10.4)

    paragraph = doc.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.paragraph_format.space_after = Pt(1.8)
    run = paragraph.add_run(contact)
    run.font.size = Pt(8.85)
    run.font.color.rgb = RGBColor(60, 60, 60)

    for section in sections:
        section_name = section['name']
        items = section['items']
        add_section(section_name)

        if section_name == 'Selected AI Projects':
            i = 0
            while i < len(items):
                if items[i].startswith('### '):
                    add_entry(items[i][4:].strip())
                    i += 1
                    if i < len(items) and items[i].startswith('**'):
                        add_tech(clean_bold(items[i]))
                        i += 1
                    while i < len(items) and items[i].startswith('- '):
                        add_bullet(items[i][2:].strip())
                        i += 1
                else:
                    i += 1

        elif section_name == 'Experience':
            i = 0
            while i < len(items):
                if items[i].startswith('### '):
                    entry = items[i][4:].strip()
                    i += 1
                    date = None
                    if i < len(items) and items[i].startswith('**'):
                        date = clean_bold(items[i])
                        i += 1
                    add_entry(entry, date)
                    while i < len(items) and items[i].startswith('- '):
                        add_bullet(items[i][2:].strip())
                        i += 1
                else:
                    i += 1

        elif section_name == 'Education':
            i = 0
            while i < len(items):
                if items[i].startswith('### '):
                    entry = items[i][4:].strip()
                    i += 1
                    date = None
                    meta = ''
                    if i < len(items) and items[i].startswith('**'):
                        match = re.match(r'\*\*(.*?)\*\*\s*\|\s*(.*)', items[i])
                        if match:
                            date, meta = match.group(1), match.group(2).rstrip('  ')
                        else:
                            date = clean_bold(items[i])
                        i += 1
                    add_entry(entry, date)
                    paragraph = doc.add_paragraph(style='ResumeMeta')
                    paragraph.paragraph_format.space_after = Pt(0.4)
                    if meta:
                        paragraph.add_run(meta)
                    if i < len(items) and items[i].startswith('Thesis:'):
                        if meta:
                            paragraph.add_run(' | ')
                        thesis = items[i][len('Thesis:'):].strip().strip('*')
                        paragraph.add_run('Thesis: ')
                        run = paragraph.add_run(thesis)
                        run.italic = True
                        i += 1
                else:
                    i += 1

        elif section_name == 'Technical Skills':
            for item in items:
                if not item.startswith('- '):
                    continue
                text = item[2:].strip()
                match = re.match(r'\*\*(.*?):\*\*\s*(.*)', text)
                paragraph = doc.add_paragraph(style='ResumeMeta')
                paragraph.paragraph_format.space_after = Pt(0.35)
                if match:
                    run = paragraph.add_run(match.group(1) + ': ')
                    run.bold = True
                    paragraph.add_run(match.group(2))
                else:
                    paragraph.add_run(text)

    for paragraph in doc.paragraphs:
        if paragraph.style.name in ('ResumeSection', 'ResumeEntry', 'ResumeTech'):
            paragraph.paragraph_format.keep_with_next = True
        p_pr = paragraph._p.get_or_add_pPr()
        if p_pr.find(qn('w:widowControl')) is None:
            widow = OxmlElement('w:widowControl')
            widow.set(qn('w:val'), '0')
            p_pr.append(widow)

    doc.save(out_path)


if __name__ == '__main__':
    build_docx(*parse_source(SOURCE), OUT)
    print(OUT)
