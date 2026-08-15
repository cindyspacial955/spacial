# The Japan Edit — Shopee MY Seller Centre 実装ワークシート（2026-08）

**作成日：2026-08-15**
**元仕様：** `The_Japan_Edit_Shopee_MY_Seller_Centre_Implementation_Spec_2026-08-15.md`
**元実行指示：** `The_Japan_Edit_Claude_Shopee_Direct_Execution_Prompt_2026-08.md`

## この文書の位置づけ

自動実装が実行できなかったため（→ 末尾「実行不能の記録」）、**Seller Centre を開いた人が上から順に処理すれば完了する**形に仕様を再構成した。判断は全て事前に確定済みで、作業者が仕様書を読み返す必要はない。各ステップの `[ ]` を潰していけば終わる。

**変更してよい範囲：** Shop Profile / Shop cover / Shop Description / Shop Announcement（項目がある場合のみ）/ Shop Categories / Shop Decoration / FAQ Assistant。
**絶対に触らない：** 商品情報・価格・在庫・送料・Voucher/広告・銀行口座・法人/税務情報・本人確認・注文/返金・チャット履歴・スタッフ権限。

---

## STEP 0 — 事前確認（作業開始前に3分）

- [ ] ログイン中のストアが **The Japan Edit / Shopee Malaysia** であることを画面上部で確認する。違えば作業しない。
- [ ] 承認済み画像ZIP `The_Japan_Edit_Final_Shopee_Assets_2026-08.zip` を手元に展開し、下記10ファイルが揃っているか確認する。

| ファイル | 想定サイズ | 用途 |
|---|---:|---|
| `TJE_shop_cover.jpg` | 1200×600 | Shop cover |
| `TJE_hero_edit_2026-08.jpg` | 1200×600 | Hero Banner |
| `TJE_cat_trending.jpg` | 1200×1200 | Trending in Japan |
| `TJE_cat_new.jpg` | 1200×1200 | New from Japan |
| `TJE_cat_matcha.jpg` | 1200×1200 | The Matcha Edit |
| `TJE_cat_snacks.jpg` | 1200×1200 | Japanese Snacks & Sweets |
| `TJE_cat_beauty.jpg` | 1200×1200 | Beauty & Self-Care |
| `TJE_cat_character_limited.jpg` | 1200×1200 | Character & Limited Finds |
| `TJE_cat_lifestyle.jpg` | 1200×1200 | Lifestyle from Japan |
| `TJE_cat_seasonal.jpg` | 1200×1200 | Seasonal Japan |

- [ ] ロゴは**変更しない**（`TJE_logo_square.png` は今回の納品に含まれない）。
- [ ] 古い静物版Heroや旧カテゴリ画像が手元にあっても**使わない**。上表が最終版。
- [ ] Section banner（A14〜A18）は未制作。**代替のテキストだけのセクションを作らない。**
- [ ] 変更前スクリーンショットを撮る：`01_profile_before`、`03_categories_before`、`05_decoration_desktop_before`、`06_decoration_mobile_before`。

---

## STEP 1 — Shop Profile

**場所：** Shop > Shop Profile / Shop Information

- [ ] **Shop name：** `The Japan Edit` のまま。変更しない。
- [ ] **Shop logo：** 現行のまま。変更しない。
- [ ] **Shop cover：** `TJE_shop_cover.jpg` をアップロード。
  - トリミングは Shopee が要求する場合のみ。静物のまとまり全体が残るようにし、カテゴリの幅が消えるほど寄せない。
- [ ] **Shop Description：** 下記を**そのまま全文**貼り付ける。

```
The Japan Edit is a Japan-based curated shop bringing Malaysia products that are genuinely gaining attention in Japan now. We source through trusted Japanese retailers and select each item for relevance, quality and story—from matcha and snacks to beauty, lifestyle and limited finds. Direct from Japan. Questions or product requests? Chat with us.
```

- [ ] **Shop Announcement：** 画面に項目が**ある場合のみ**、下記を貼り付ける。

```
NOW EDITING: Matcha from Japan | New finds added regularly | Direct from Japan | Follow our shop to see the next edit.
```

  - 項目が**ない場合はスキップ**し、報告書に `Not available in this account` と記録する。
  - **この一文を Shop Description の冒頭に入れてはいけない。**
- [ ] 保存。`02_profile_after` を撮る。

---

## STEP 2 — Shop Categories

**場所：** Shop > Shop Decoration > Category Page > Edit

この順番で作成／既存分を突き合わせる。**重複を作らない。**

| # | Category name | 選定方式 | 買い手向け表示ONの条件 |
|---:|---|---|---|
| 1 | `Trending in Japan` | Manual のみ | 証拠基準を満たす商品2点以上 |
| 2 | `New from Japan` | Rule-based（正確に表現できる場合のみ）／不可なら Manual | 直近30日出品かつ在庫あり2点以上 |
| 3 | `The Matcha Edit` | Manual | 商品があれば即ON |
| 4 | `Japanese Snacks & Sweets` | Manual | 2点以上 |
| 5 | `Beauty & Self-Care` | Manual | 2点以上 |
| 6 | `Character & Limited Finds` | Manual | 2点以上＋限定根拠確認 |
| 7 | `Lifestyle from Japan` | Manual | 2点以上 |
| 8 | `Seasonal Japan` | Manual | 2点以上。季節終了でOFF |
| 9 | `Editor's Picks` | Manual | 3〜4点選定して即ON |
| 10 | `All Products` | Shopee標準 | 標準導線があれば**新規作成せず流用** |

**商品の入れ方**

- `Trending in Japan`：**売りたいから入れる棚ではない。** 日本国内の異なる2種類以上の現在シグナル（うち1つは30日以内）が既存リサーチにある商品だけ。根拠がなければ空のまま作成のみ。
- `New from Japan`：ライブUIが「この店で直近30日出品かつ在庫あり」を正確に表現できる場合のみルール指定。できなければ出品日を確認して手動。
- `The Matcha Edit`：有効・在庫ありの抹茶商品を全て手動で入れる。
- `Japanese Snacks & Sweets` / `Beauty & Self-Care` / `Lifestyle from Japan`：有効・在庫ありの該当商品。
- `Character & Limited Finds`：キャラクター商品と、公式に限定と確認できる商品のみ。
- `Seasonal Japan`：メーカーが季節商品と明示、または明確に今の季節用途があるものだけ。
- `Editor's Picks`：今の店を最もよく表す有効・在庫あり商品を3〜4点。カテゴリの幅が出るように選ぶ。売上実績を装わない。

**共通ルール**

- [ ] 構造は将来分も含めて**今すぐ全部作る**。商品が足りないカテゴリは作成だけして買い手向け表示をOFF。
- [ ] **空のカテゴリを公開しない。**
- [ ] 1商品が入るテーマカテゴリは最大3つ＋`All Products`。
- [ ] 既存カテゴリのリネーム／並べ替えは、商品やユーザー作成の整理を壊さない場合のみ。**リネーム前に現在の名前と商品数を記録する。**
- [ ] `04_categories_after` を撮る。

---

## STEP 3 — Shop Decoration

**場所：** Shop > Shop Decoration

既存コンポーネントのうち、**有効なキャンペーン義務やこのタスクの範囲外のユーザー作成コンテンツは残す。**

この順に構築し、**公開条件を満たさないものは作らずに飛ばす**（プレースホルダー禁止）。

| # | コンポーネント | 設定内容 | 追加条件 |
|---:|---|---|---|
| 1 | Voucher | 既存の有効Voucherを表示するだけ | 有効Voucherが既にある場合のみ。**Voucherの作成・編集は禁止** |
| 2 | Hero Banner / Carousel | `TJE_hero_edit_2026-08.jpg` | 必須 |
| 3 | Category「SHOP BY EDIT」 | 8タイル（下記順） | 必須 |
| 4 | Product Highlight「TRENDING IN JAPAN NOW」 | Manual 3〜4点 | 証拠基準を満たす商品が2点以上ある時だけ |
| 5 | Product Highlight「NEW FROM JAPAN」 | Manual または検証済みルール | 対象3点以上 |
| 6 | Products by Category「THE MATCHA EDIT」 | `The Matcha Edit` にリンク | 抹茶商品が有効なら必須 |
| 7 | Product Highlight「EDITOR'S PICKS」 | Manual 3〜4点（有効・在庫あり） | 必須 |
| 8 | Top Products「BEST SELLERS AT THE JAPAN EDIT」 | — | **開始時は追加しない。** 自店の実注文データが3商品以上ある場合のみ |
| 9 | Seasonal / Limited | Seasonalカテゴリタイルまたは標準タイトル | 対象3点以上。**正方形タイルを横長に引き伸ばさない** |
| 10 | Why The Japan Edit / About Us | 下記About Us全文 | Custom Page か適切なテキストコンポーネントがある場合のみ |

**Hero に表示される文字（画像内、確認のみ）**

```
THE JAPAN EDIT
What's Trending in Japan, Curated for You.
SUMMER EDIT 08.2026
```

**Hero のリンク先（この優先順で最初に存在するもの）**
1. `Trending in Japan`
2. `The Matcha Edit`
3. ショップホーム / `All Products`

**Category コンポーネントのタイル順とファイル対応**

| 順 | カテゴリ | 画像ファイル |
|---:|---|---|
| 1 | Trending in Japan | `TJE_cat_trending.jpg` |
| 2 | New from Japan | `TJE_cat_new.jpg` |
| 3 | The Matcha Edit | `TJE_cat_matcha.jpg` |
| 4 | Japanese Snacks & Sweets | `TJE_cat_snacks.jpg` |
| 5 | Beauty & Self-Care | `TJE_cat_beauty.jpg` |
| 6 | Character & Limited Finds | `TJE_cat_character_limited.jpg` |
| 7 | Lifestyle from Japan | `TJE_cat_lifestyle.jpg` |
| 8 | Seasonal Japan | `TJE_cat_seasonal.jpg` |

- 空の遷移先が買い手に露出してしまう仕様なら、STEP 2 の表示条件を満たすタイルだけ出す。

**About Us 全文（該当コンポーネントがある場合のみ）**

```
Not everything from Japan makes the edit.

We live and source in Japan, watching what is newly launched, selling out, showing up in stores and earning real attention. Then we select the finds worth sending to Malaysia.

Every product in The Japan Edit is chosen for a reason: relevance, quality, usefulness, taste or a story you will want to discover. Today, the edit begins with Japanese matcha. Next, it grows with snacks, beauty, lifestyle and limited finds from across Japan.

Authenticity is the starting point. Curation and timing are what make it The Japan Edit.
```

- [ ] デスクトップとモバイルのレイアウトが別なら**両方**設定する。
- [ ] Shopee のプレビュー用トリミングを使い、**縦横比を歪めない。**
- [ ] Follow バナーを捏造しない。A14〜A18 の代わりのテキストセクションを作らない。
- [ ] `07_decoration_desktop_after`、`08_decoration_mobile_after` を撮る。

---

## STEP 4 — FAQ Assistant

**場所：** Chat Management > FAQ > FAQ Card

既存の質問と突き合わせ、同義のものを重複登録しない。**上限まで、この優先順で**登録する。

**1. Are your products authentic?**
```
Yes. We source our products in Japan through official brand stores or established Japanese retailers. We keep procurement records and never list replicas or unverified goods.
```

**2. Where do you ship from?**
```
Our items are sourced and dispatched from Japan. Please check the delivery estimate shown by Shopee at checkout for your order.
```

**3. How do you choose products?**
```
We look at new launches, current retail activity, trusted rankings, seasonal demand and genuine customer interest in Japan. We then select products for relevance, quality, usefulness and story.
```

**4. Are all food products Halal-certified?**
```
No. We state "Halal-certified" only when valid certification can be verified. "Muslim-friendly" does not mean Halal-certified. Please check each listing and message us before ordering if you need help.
```

**5. Where can I check ingredients and allergens?**
```
Please check the product listing and package images. Ingredients and allergen information may be printed in Japanese. If you have an allergy or dietary restriction, message us before ordering; the manufacturer's package information remains the authoritative source.
```

**6. Is every item "trending in Japan"?**
```
No. "Trending in Japan" is used only for products with current supporting evidence. Other items may be marked New from Japan, Seasonal, Limited Edition or Editor's Pick.
```

**7. Can I request a product from Japan?**
```
Yes. Send us the product name, brand or a clear photo through Shopee Chat. We review requests based on availability, shipping suitability and Malaysia import requirements. A request does not guarantee listing or stock.
```

**8. What if an item is limited or sold out in Japan?**
```
Limited items can sell out without notice. If we cannot secure an ordered item, we will follow Shopee's order and refund process and contact you through Shopee Chat.
```

- [ ] **配送日を固定で断言しない。**
- [ ] **全食品がHalal認証済みと書かない。**
- [ ] `09_faq_after` を撮る。

---

## STEP 5 — 公開前QA（全項目パスで公開）

- [ ] Shop name が `The Japan Edit` のまま。
- [ ] カバーが承認済みの文字なし静物。
- [ ] Hero が承認済みの夏アニメ版で、比率が歪んでいない。
- [ ] Hero の文字がモバイル・デスクトップ双方で読める。
- [ ] 最初の1画面で「今の日本」「厳選」「日本調達」が伝わる。
- [ ] 8タイルが上表のファイル対応どおり。
- [ ] 画像内とカテゴリ名の `SEASONAL JAPAN` の綴りが正しい。
- [ ] 公開されている全カテゴリに、有効・在庫ありの商品が2点以上ある。
- [ ] 空の Product Highlight、在庫切れだけの棚がない。
- [ ] Hero とカテゴリのリンクが意図した Shopee 内の遷移先を開く。
- [ ] `Trending` / `New` / `Limited` / `Halal-certified` / `Best Sellers` を根拠なしに使っていない。
- [ ] 外部連絡先やShopee外取引への誘導を追加していない。
- [ ] FAQ が配送時期を固定で約束していない。
- [ ] モバイル・デスクトップのプレビューで、必要な文字や顔が切れていない。
- [ ] 範囲外の既存設定と商品データが変わっていない。

**全てパスしたら、追加の確認を挟まず Publish する。** Shopee 側の通常の Save/Publish 確認ダイアログは承認してよい。
- [ ] `10_publish_confirmation` を撮る。

---

## 停止条件（該当したら安全に止めて具体的に報告）

- 認証（ログイン / CAPTCHA / 2FA / パスキー / 端末確認）で手動引き継ぎが必要 → **これだけは想定内の手動作業。**認証後は同じ画面から再開する。**パスワード・OTP・復旧コードをチャットに書かない。**
- 編集または公開の権限が不足している。
- 承認済み画像やコピーを変えないと解消できないアップロード／保存／公開エラーが出る。
- 既存のカテゴリ／コンポーネントに、置き換えると破壊的または判断が割れるユーザー作成コンテンツがある。
- UI上の制限で、指定コピーが実質的に収まらず、代替フィールドもない。
- アカウント／ストアが The Japan Edit / Malaysia と一致しない。
- 禁止領域に触れる操作が必要になる。

認証以外で止まった場合は、**完了済みの変更をドラフトとして保存したまま**残す。完了させるために既存コンテンツを消さない。

---

## 証跡の保存先

`research-runs/2026-08-15_tje-shop-implementation/` に、STEP中で指定した10点（`01_profile_before` 〜 `10_publish_confirmation`）を PNG/JPG/PDF で保存する。パスワード、OTP、入金情報、不要な買い手情報は含めない。スクリーンショットが保存できない場合は、確認したページと見えていた内容を文章で記録する。

---

## 実行不能の記録（2026-08-15、自動実装の試行）

仕様書の「Claudeによる直接実装」は、この実行環境では**開始できなかった**。停止条件によるものではなく、環境側の制約。

| 必要な前提 | 実測結果 |
|---|---|
| Seller Centre へのブラウザ到達 | **不可。** `shopee.com.my:443` / `seller.shopee.com.my:443` ともにネットワークポリシーで CONNECT が 403 拒否（agent proxy の `recentRelayFailures` に `connect_rejected` として記録） |
| `The_Japan_Edit_Final_Shopee_Assets_2026-08.zip` | **未提供。** 添付は仕様書2点のみ |
| 既存プロジェクト（`shopee-ec` / `CLAUDE.md` / `matcha_shopee_product_master_20260811.xlsx`） | **不在。** `~/Documents` 自体が存在しない |
| 接続中リポジトリ | `cindyspacial955/spacial`（コワーキング営業案件。The Japan Edit とは無関係） |

到達できないため、認証の手動引き継ぎでも解消しない（ログイン画面に到達できない）。

**実行するには次のいずれかが必要：**
1. `shopee.com.my` / `seller.shopee.com.my` への到達が許可された環境で実行する。
2. Seller Centre にログイン済みのローカル環境で Claude Code を動かし、承認済みZIPと既存 `shopee-ec` プロジェクトを同じ作業フォルダに置く。
3. 本ワークシートに沿って手動で設定する（判断は全て確定済みのため、仕様書を読み返す必要はない）。
