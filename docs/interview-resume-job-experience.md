# Resume Interview Drill — Kahap Job Experience

更新：2026-10-18。這是歷史原始碼靜態考古；未啟動舊系統、寄信、執行 migration／worker／排程、連接舊正式機或部署。詳讀 [SuggestionBox source archaeology](https://github.com/kolihhan/job-project/blob/main/docs/suggestionbox-code-archaeology.md) 和 [Career source archaeology](https://github.com/kolihhan/job-project/blob/main/docs/career-code-archaeology.md)。

所有 suggestionbox/、career/ 路徑相對於私有原始碼 repo [kolihhan/job-project](https://github.com/kolihhan/job-project)。本文件以真實程式證據取代原先待考古的假設；未證明的個人操作仍保留 USER／UNKNOWN。

## 證據規則

- **CODE**：source 直接實作，不等於已證明正式環境成功運作。
- **CONFIG**：manifest／lock／設定／部署文件／Git metadata；區分設定意圖和實際運行。
- **USER**：本人回憶的設計、實作、上線、維護、搬遷。source 不能單獨證明操作者。
- **INFERENCE**：有依據的解釋、風險或建議，不能改說成親歷事實。
- **UNKNOWN**：沒有充分證據，留待回憶或補紀錄。

## 先記住的事實與修正

| 面試主題 | 確認結果 | 可重查的 repository 路徑 |
|---|---|---|
| Archive identity | Forum tar = SuggestionBox；Laravel zip = Career | 兩案 composer/package、README、views、routes |
| SuggestionBox stack | Laravel **9.36.4**、Livewire **2.10.7**；沒有 Vue dependency | `suggestionbox/composer.lock`、`suggestionbox/package.json` |
| Career stack | Laravel **5.8.38**、Vue **2.7.16**、Vuex **3.6.2**、Router **3.6.5**、Axios **0.18.1** | `career/composer.lock`、`career/package-lock.json` |
| SuggestionBox互動 | Blade/controller 表單 + 四個 Livewire 元件；不是全部操作都走 Livewire | `suggestionbox/app/Http/Livewire/`、`suggestionbox/routes/web.php` |
| Career互動 | Vue/Vuex/Axios/JWT API；管理端另有 Blade/jQuery | `career/resources/assets/vue/`、`career/resources/views/admin/`、`career/public/js/admin/` |
| 成案門檻 | **100 筆總 Message，含贊成和反對**，不是100贊成 | `suggestionbox/app/Http/Livewire/Front/Vote/Detail.php::submit` |
| SuggestionBox通知 | 同步 HTTP 呼叫 Career `/third-place-sendEmail`；未見自寫 Jobs／worker | 同上；`suggestionbox/app/Http/Controllers/Admin/VoteManageController.php::process` |
| Career佇列 | 封存 production 設定是 **database queue、Redis cache** | `career/config/queue.php`、`career/config/cache.php`；Career考古文件安全env摘錄 |
| Queue工作 | 無自寫 `app/Jobs`，但 ShouldQueue notification 會由框架變成 queued job | `career/app/Notifications/StudentCareerLectureNotification.php` |
| SSL / production OS | **USER-CONFIRMED:** SuggestionBox production 由本人用 **Certbot + Let’s Encrypt** 配 HTTPS；production 曾用 **Ubuntu 22.04 / 24.04**。`forceScheme` 仍只算 application-side CONFIG。Career README 另有 Certbot check/renew＋Nginx restart。 | Career README、SuggestionBox provider；本人確認的 production 操作 |
| Career 個人歸屬 | `career-git.zip` 補回完整 Git history；本人確認 `kolihhan`、`kolih`、`LIH HAN KO`、`高立恒`、`DESKTOP-96L42D8\lihha` 全是本人。五個 identity 合計 **516 / 1,176 commits**，範圍 **2022-08-04 → 2026-08-31**。 | `job-project/docs/career-code-archaeology.md` 的 Git-confirmed ownership section |

以上是 lock 的解析版本，不是即時正式機盤點。**CONFIG** 原始被排除 `.env` 的安全白名單：SuggestionBox=`local`、MySQL、sync queue、file cache/session；Career=`production`、MySQL、database queue、Redis cache、file session、`APP_POTOCOL=https`。不發布原env或其他秘密值；此摘錄也不證明現在有worker正常執行。

## SuggestionBox：必須能講清楚的資料流

**CODE** 身份：`suggestionbox/routes/web.php` → `StudentController::loginTo` → Career `/third-place-login` → 本地 `Student` 身份對應 → student session。Admin 是另一個 guard。不是所有密碼驗證都由Forum自行實作。

**CODE** 提案：proposal route → `ProposalController::{tempPreview,preview,storeTemp,store}` → handler內Validator → `TempProposal`/`Proposal`及附件表 → public disk → redirect到投票清單。主旨／說明／建議必填；單檔10,240KB，jpeg/png/gif/pdf。預覽先存暫存，確認再建立正式案號。位置：`suggestionbox/app/Http/Controllers/ProposalController.php`、`suggestionbox/resources/views/front/proposal/`。

**CODE** 投票：`VoteController::show` → Blade 掛 `Front\Vote\Detail` → Livewire `submit()` → Message → 總聲量 → `status/process/email_status` → 同步Career通知 → browser event／Livewire refresh。管理員用 `VoteManageController::process` 受理／結案／改說明與通知。

**CODE** DB：Student有Proposal／Message；Proposal有Messages、附件、UnitItem；UnitItem屬Unit。草稿／草稿附件另表。細節在 `suggestionbox/app/Models/` 和 `suggestionbox/database/migrations/`；業務關聯不代表每條FK、唯一限制、授權檢查都完善。

**解釋Livewire：** Blade先顯示頁面，互動請求回PHP元件，元件改狀態或DB，回傳UI更新。本案表單仍走controller，清單／投票／留言／部分管理互動才是Livewire。歷史選型理由若忘了，不能用今天的技術比較冒充當年決策。

## Career：必須能追通的一條完整流程

**CODE** 講座報名：`career/resources/assets/vue/components/pages/lectures/LectureContent.vue` → `common/modal/StudentEnrollEvent.vue`驗證與emit → `store/pages/students.js` action → `services/api/students.js` → Axios Bearer token → `career/routes/api.php` 的 `POST /api/student/career-lecture` → `StudentCareerLectureController::store` → 時段／欄位／重複檢查 → `CareerLecture::students()` 寫 `career_lecture_student` pivot → `StudentCareerLectureNotification` → JSON message → Vue更新歷史／導頁。

**CODE** API主設定：`career/resources/assets/vue/services/api/index.js`；JWT刷新：`career/app/Http/Middleware/RefreshToken.php`。這條controller直接用Eloquent，沒有憑空加一層PHP service；實習表單才有 `career/app/Service/InternFormService.php` 等服務。DB其他域包含Enterprise→JobList、徵才表單／攤位／商品、學生／教師／企業的實習表單。

**CODE／界線** 正取／候補存在pivot；取消可遞補。報名通知dispatch在attach／commit前，個人資料更新也在transaction前。不能說全副作用after-commit，不能由transaction推論一定不超賣或所有檔案／郵件都能rollback。

## Career：Git-confirmed 本人實際做過的東西

`CONFIG + USER-CONFIRMED IDENTITY`：額外提供的 `career-git.zip` 是完整 Career Git history。以下五個 author identity 全部由本人確認是自己：

- `kolihhan <ko.lih@kahap.com>` — 306 commits
- `kolih <ko.lih@kahap.com>` — 108 commits
- `DESKTOP-96L42D8\lihha <lihhanko3@gmail.com>` — 93 commits
- `高立恒 <ko.lih@kahap.com>` — 7 commits
- `LIH HAN KO <ko.lih@kahap.com>` — 2 commits
- **Total: 516 unique commits / repo 1,176 commits**
- **Date range: 2022-08-04 → 2026-08-31**

這代表 Career 不應再描述成「只改一點 CSS」。Git 直接支持本人長期做大量 production maintenance、bug fixing 與 feature work。最適合面試記憶的 commits：

| Commit | 直接可說的工作 |
|---|---|
| `57352fe0` | 第三方後台登入功能；auth/controller/route 類修改 |
| `9b45ef74` | 實習老師 API：學生資料、實習紀錄、實習機構列表 |
| `c398c2c3` | 使用者修改密碼流程修正；簡單 maintenance/debug 例子 |
| `ff6eb4a8` | 學生集點紀錄活動類型錯誤顯示修正 |
| `25477bc3` | 企業申請實習時自動帶入既有資料；跨 Laravel API + Vue/store/API service |
| `6cc473ea` | API 報錯、表單欄位與 model/resource/schema 類調整 |
| `18abd37d` | 真實 CSS/UI design 維護；CSS 只是整體工作的一小部分 |
| `0c830242` | 企業更新資料判斷 + 前後台校園徵才活動一致性修正 |

**安全說法：**「我接手一個既有 Laravel/Vue production system，長期做 bug fixing、API/表單/實習/點數/admin/front-end 功能維護與新增。」不要把其他作者 commits 或整個平台全部功能都說成自己從零寫。

## Pac Com：簡短準備，不與 Career 混用

`USER`：Pac Com 是更早期的實習，主要在既有 **Laravel + Vue POS** 系統做簡單 maintenance：小型 bug fix、UI/CSS/layout 調整、既有功能維護。這段經歷的主要學習價值是第一次在真實專案裡理解並使用 Laravel framework。

目前沒有找到可對應 Pac Com 的 source repo 或 Git history；`career-git.zip` 明確是 2022-08 之後的 NTUST Career history，**不能拿 Career commits 冒充 Pac Com**。

面試安全版：

> At Pac Com I worked on an existing Laravel/Vue POS system. The tasks were relatively straightforward: maintaining existing features, fixing smaller application or UI issues, and making CSS/layout adjustments. It was where I first learned how a real Laravel application is structured and maintained.

如果被追 Laravel，講你當時建立的基礎 mental model：route → controller → model/database → Blade/Vue response；不要虛構複雜 production incident。

## Queue vs job vs worker vs scheduler／cron

| 名詞 | ELI5 | 本專案具體證據 |
|---|---|---|
| Job | 一項要做的工作 | Career框架queued notification；沒有自寫Jobs目錄 |
| Queue | 保存等待工作的backend | Career原production env選database；jobs/failed_jobs migrations；SuggestionBox原env選sync |
| Worker | 持續拿工作來執行的process | `career/environment/supervisord.d/laravel-worker.conf`：queue:work、3processes、sleep3、tries3、autorestart |
| Scheduler | 決定定期工作何時到期 | 兩案 `app/Console/Kernel.php` |
| Cron | OS可用來定時啟動命令的機制 | Career實際checked-in配置是Supervisor每60秒呼叫schedule:run，不是已確認的crontab |

**CODE** SuggestionBox：daily `proposal:check`；`suggestionbox/app/Console/Commands/CheckProposalExpiry.php` 處理過期未成案與草稿附件。正式機如何觸發／有沒有成功執行仍UNKNOWN。

**CODE/CONFIG** Career：daily17:00徵才報名／選位通知；daily01:00 sitemap和`lectures:clear`。後者清除已結束且開啟隱私模式活動pivot的生日／身份欄位；不等於抹掉所有個資。`line:check`有command，卻未在Kernel安排。`StudentCareerLectureNotification` implements ShouldQueue；`StudentMailRegisterToken`只有Queueable trait，不能說所有mail都queued。

**INFERENCE／面試診斷** Worker死掉可能jobs堆積、HTTP成功但mail沒寄。檢查Supervisor、jobs/failed_jobs、Laravel log、SMTP。retry可能重複副作用；3workers或email_status都不是exactly-once保證。這是理解方法，只有USER記憶／事故紀錄能證明你實際處理過。

## MySQL、搬機與SSL

**CODE/CONFIG** SuggestionBox主要讀 `DB_CONNECTION/HOST/PORT/DATABASE/USERNAME/PASSWORD`；Career主要讀 `DATABASE_CONNECTION/HOST/PORT/NAME/USER/PASSWORD`，見各自`config/database.php`。Career舊`.env.local.docker`卻是DB_*與QUEUE_DRIVER；現有config讀DATABASE_*與QUEUE_CONNECTION。直接搬舊env可能完全沒設定到使用中的連線，這是具體可見風險，不是已證明的親歷故障。

**CONFIG** Career有Docker／Envoy／CI／Nginx-FPM-Swoole／Supervisor等多年代配置。Dockerfile PHP7.4 Apache和README PHP7.2／Nginx-Swoole並存；不能拼成已驗證的一套正式拓樸。外部CI template／deploy.sh缺失。`career/README.md:97–103`記錄mail卡住時查Supervisor、SSL過期時`certbot certificates`／`certbot renew`／Nginx restart。

**USER-CONFIRMED** SuggestionBox production deployment 由本人負責；production 曾跑在 **Ubuntu 22.04 / 24.04**，HTTPS 使用 **Certbot + Let’s Encrypt**。Career 亦有本人搬 server／HTTPS 的記憶，且 README 有 Certbot/Nginx 維運背景。**UNKNOWN** 仍包括每次搬遷的舊新機對應版本、完整 backup/restore、media 搬法、DNS cutover／TTL、停機、rollback、驗收，以及當時 Certbot plugin/challenge 的精確選項。資料 migration 檔不是 server migration 紀錄。

**SSL概念** DNS→驗證網域控制權→CA簽憑證→web server載入憑證與私鑰→HTTPS→定期續期與重新載入。`URL::forceScheme()`只改生成網址，不會簽憑證、設定TLS或保證續期。兩案讀的是拼字原樣`APP_POTOCOL`。SuggestionBox HSTS類別的header語句是註解，不能說已生效。

**INFERENCE／用來喚回記憶的搬遷順序：** 盤點runtime／DB／uploads／secrets／web／workers／scheduler → 備份並確認可還原 → 準備相容環境和權限 → 配置正確env與APP_KEY、還原資料／storage link、清cache → 測登入／讀寫／附件／活動／mail／背景工作 → 切DNS並配置HTTPS → 看logs、保留rollback、驗收後收舊機。只有當年真做過的步驟才用第一人稱。

可能壞在哪：PHP/extensions、DB帳密或grants、host/port、舊env鍵、schema mismatch、缺uploads／storage權限、APP_KEY更動、stale config cache、舊worker未reload、兩機重複scheduler、SMTP阻擋、DNS未切、憑證網域不符／過期／沒載入。不要把這份風險清單說成全部親歷。

## Production／DB debugging：要準備一件真的事件

**CONFIG/Git + USER-CONFIRMED IDENTITY** SuggestionBox 的 `kolihhan`／相關已確認本人 alias commits 可作個人貢獻證據；`a997328`／`e331dff`涉及 email_status 和重複通知，`a9a4be5`涉及成案／留言。Career 另有 516 個本人確認 commits，包含密碼、API、點數、實習、表單、UI 等大量真實 maintenance。commit subject 是回憶入口，仍不要把 subject 擴寫成沒發生過的事故故事。

**CODE／本次靜態發現** Proposal validation用strip_tags副本，persist卻讀原request；Career通知早於commit；legacy MD5登入沒有自動升級hash；QR payload是base64 JSON，不代表加密防竄改。它們不是本次修復，也未證明是你當年的修復。

**INFERENCE／debug方法** 明確症狀與範圍→時間/log/stack→最近變動→沿route/auth/validation/query/env定位→最小根因修正→驗證原案例和旁邊流程。DB先分連線、schema、資料、query、constraint、效能、transaction，不要一問DB就說加index。

**USER待補** 症狀？你第一個看什麼證據？根因？改哪檔／設定／資料？怎麼驗證？如何防再發？實際成果？沒有真記憶就不能用靜態風險補故事。

## 個人可以安全說什麼

| 敘述 | 證據與界線 |
|---|---|
| 參與SuggestionBox 0→1設計／實作／上線 | USER；歷史Git多人，個人責任要具體，不說全程式獨寫 |
| 解釋附件、投票、通知狀態、每日清理、Excel、雙語 | CODE；kolihhan commit提供多項歸屬線索，確認本人alias後挑本人部分講深 |
| 接手Career、加功能、搬server、處理HTTPS | USER；沒有Git，快照差異不能指定作者 |
| 解釋queue／Supervisor／schedule／Certbot文件 | CODE/CONFIG；個人操作和成功結果仍要記憶或紀錄 |
| 指出現有缺陷及更好的做法 | 可以，但說是現在重讀的判斷，不假稱當年已完成 |

## 口述稿：30秒與2分鐘

以下個人責任部分來自USER，必須按真實分工調整。

### SuggestionBox：30秒

「我參與台科大學生建言平台從設計到實作和上線，用Laravel與Livewire。學生能提案、預覽、附檔、投票留言，管理員能受理、分派單位、結案與匯出。帳號和狀態通知整合既有Career API。這是團隊開發，我會區分自己負責的功能。」

### SuggestionBox：2分鐘

「這個平台讓學生建言有完整的追蹤流程。我參與設計和實作，學生先填主旨、說明及建議，可附圖片或PDF；預覽寫暫存提案與附件紀錄，確認再轉正式提案、產生案號。主要表單走Laravel controller，投票列表、留言和部分管理操作用Livewire，互動回到PHP元件，改DB和狀態後更新UI。

投票和留言是一筆Message，贊成與反對都算聲量，達100筆後成案。管理員再受理、指定權責單位、更新說明或結案，也能匯出Excel。身份驗證共用Career API，本地保留身份對應和session；狀態通知也是同步呼叫Career，不是這個專案自己的背景job。email_status記錄通知進度，另有每日命令處理未成案到期、草稿與附件清理。

現在我能解釋資料流和錯誤邊界，例如DB transaction不能把檔案或外部API副作用一起回滾。歷史Git也能對回附件、投票、通知狀態和雙語等功能。我不會把同事的初始程式都認領；部署和HTTPS的細節則按當年的實際操作補充。」

### Career：30秒

「Career是接手維護的既有台科大職涯平台，Laravel後端、Vue前台，管理端另有Blade。我做功能維護，也處理server搬遷和HTTPS。它有學生、企業、教師帳號及活動、徵才、實習、通知。我會用具體功能和真實維運案例說明工作，不把整個既有平台當成自己的作品。」

### Career：2分鐘

「這個專案是接手既有系統，跟SuggestionBox不同。Vue前台用Vuex管狀態，API service經Axios呼叫Laravel並帶JWT，管理端有Blade和jQuery。範圍很大，所以接手要先沿一條產品流程理解它。

以講座報名為例，Vue表單驗證後呼叫store action與API；後端檢查時間、必填和重複報名，按名額決定正取或候補，再寫學生和講座的pivot並發通知。取消時會從候補遞補。這條流程能一起說明前端狀態、後端身份驗證、DB關係與副作用邊界。

維運方面，封存production設定是database queue，Redis作cache；Supervisor配置三個queue workers。Scheduler另由每分鐘的runner觸發，再決定徵才通知、sitemap和隱私資料清理何時執行。搬server不能只搬code，還有DB、uploads、env鍵名、PHP相容性、權限、背景程序、DNS和HTTPS。這套程式有DATABASE_*與舊DB_*不一致的具體風險，README也有Supervisor與Certbot排障。哪個功能是我加的、哪次故障是我處理的，以及當年的切換和驗收，我會按真實記憶補充，不把所有既有功能都說成自己做的。」

## 面試官可能追問

1. 0→1原始需求？你決定哪些資料模型／技術選擇？哪個Git alias是你？
2. 畫一次proposal→draft→附件→投票→管理員結案；哪些controller，哪些Livewire？
3. 為何反對也算100門檻？後端如何防重複？UI和DB constraint有何界線？
4. Career API超時或DB rollback時，通知與本地狀態可能不同步嗎？
5. Vue component、Vuex、Axios、JWT middleware各做什麼？
6. 正取／候補怎麼存？同時搶最後名額怎麼辦？怎麼遞補？
7. Queueable和ShouldQueue差別？沒有Jobs目錄為何仍有queued jobs？
8. 哪個driver、幾個worker？worker掛掉、部署後reload、retry和重複副作用？
9. 哪些daily任務？誰呼叫schedule:run？line:check真的有排嗎？
10. DB錯誤如何區分host/port、帳密/grants、env/cache、schema、資料/query？
11. 搬機哪些state要留？APP_KEY可以換嗎？怎麼避免兩機重複工作？
12. Certbot怎麼證明domain控制權？哪個plugin/challenge？生成https URL和TLS握手差異？
13. 一件真production bug：症狀、第一證據、根因、修正、驗證和結果？
14. 哪兩個Career功能確定是你加的？快照差異為何不能證明作者？

## 紅線：不能這樣說

- 「兩個系統全部我一個人從零寫的」「merge commit／快照新增檔＝我寫的」。
- 「SuggestionBox用Vue、Redis queue、Supervisor寄通知」「Career全部mail都queued」。
- 「Career queue用Redis」；封存env選database，Redis在cache。
- 「100個贊成才成案」「retry／email_status保證exactly-once」「transaction保證不超額報名／撤銷已寄mail」。
- 「forceScheme就是SSL部署」「HSTS class存在就生效」「已證明自動續期正常」。
- 「Career QR已加密防竄改」「legacy MD5登入會自動升級hash」。
- 「migration檔就是搬機紀錄」「所有配置屬同一已驗證正式拓樸」。
- 「零停機、效能提升X%、服務1,000+人、完整測試或安全保證」：本次沒有對應量測。
- 把本次靜態風險說成當年的親歷修復，把README建議說成已執行操作。

## 復原、保密及驗證記錄

| 輸入 | 完整解出entries | member bytes | SHA-256 |
|---|---:|---:|---|
| `ntust-forum-20260608.tar(1).gz` | 10,640 | 126,736,272 | `2bcd4ff4223cb4a2dd6eaa1f7694467ba2fa1abea086b843539606f479990637` |
| `laravel-project(2).zip` | 68,998 | 936,575,376 | `6d0bf1a8f922f67d1cfc4bdf12be7b5d2a6cd4f14cc80dd735a07f53504d8859` |

Tar最後復原symlinks，未沿正式機絕對連結寫檔；ZIP全member CRC通過。完整抽取與安全發布分開：repo只保留清理後source。排除.env*、原.git、dependency、storage/records、SQL私有dump、key/certificate、nested backup及generated bundles/maps，保留72份獨特public JS/CSS。nested Career archive是舊snapshot，無nested-only own source；差異不代表作者。

清理掃描覆蓋1,605份source／8,707,665 bytes。只有7份檔案16行credential redaction，原line count、LF/CRLF保持：Career AESCrypt歷史key/IV；兩案UserFactory固定hash；Career StudentFactory、EnterpriseFactory、UserSeeder、StudentTest固定密碼。可重建_ide_helper不保留。其餘source保持原bytes與可取得mode，未refactor或升級。

掃描包含敏感路徑、provider token、private-key/certificate、credential URI、entropy候選、所有保留檔中原env秘密／AES值／fixture hash重用，搭配上下文審查。公開site key／Analytics／site-verification ID和Faker定義不當秘密；不保留真實用戶dump。結果為無已確認未清理秘密；不等於完整app security或可部署認證。

## Understand Anything 執行狀態

使用實際 `Egonex-AI/Understand-Anything` 的 `understand` skill，pinned commit `790b157028637b626c8666fa7fa28248944b900c`；skill blob `778b800c1d770ae6401ae86245def77dd220900c`。環境重置後取回原skill/scripts/core，沒有自製替代scanner/extractor或虛構graph。

兩案分開full rebuild；官方`--exclude-analysis-data`僅排除.ua等分析產物，無刪減自有source。目標流程是官方scan/import-map/Louvain batches，每批extract-structure＋file-analyzer，merge／assemble-review／architecture／tour／validation／fingerprints。Vue SFC等沒有parser的部分依skill由讀source補語義，不能冒稱AST已支援。**狀態：執行中；完成數據與限制待pipeline驗證後填入。**
