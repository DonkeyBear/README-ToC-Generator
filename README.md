# Donkey Bear's README ToC Generator

　　這是一個簡單的 Python 小程式，用於偵測 `README.md` 內的各級標題，並以其為依據生成文章目錄（ToC, Table of Contents）。

## 目錄

> * [**前言**](#前言)
> * [**相依性**](#相依性)
> * [**專案說明**](#專案說明)
>   * [README-ToC-Generator](#readme-toc-generator)
>   * [Simple-README-ToC-Generator](#simple-readme-toc-generator)
>   * [DonkeBearStyle-ToC-Generator](#donkebearstyle-toc-generator)
> * [**使用說明**](#使用說明)

## 前言

　　此專案起源於我的第一個練習專案（[Donkey Bear's Python Exercising](https://github.com/DonkeyBear/Python-Exercising-by-DonkeyBear)），由於該專案是用以整理各種練習用的程式，所以幾乎每個檔案都是一個單獨的小程式，又因為我希望能夠將這些練習用的程式當作範例，給未來的自己能在學習時供作參考，於是在 [其 README](https://github.com/DonkeyBear/Python-Exercising-by-DonkeyBear/blob/main/README.md) 內簡述了每個程式的功能，又因為手動編輯目錄的過程要一一插入錨點過於麻煩，於是寫了一個[自動將標題轉換為錨點的程式](https://github.com/DonkeyBear/Python-Exercising-by-DonkeyBear/blob/main/Misc/AnchorTrans.py)。

　　但是我仔細想了想，既然都要用程式轉換錨點了，何不乾脆將手動編輯目錄的整個過程都自動化呢？於是本專案就誕生了。

　　另外，本專案同時也是我截至目前為止獨立編寫過的最大專案（沒錯，就這麼點大小的專案，已經是我寫過最大的專案了），即使花了很多時間，還是有很多不足之處有待改進，希望大家能多多包涵。

[返回目錄](#目錄)

## 相依性

　　本專案使用了 Python 官方模組 [os](https://docs.python.org/3/library/os.html) 及非官方模組 [chardet](https://pypi.org/project/chardet/)。

[返回目錄](#目錄)

## 專案說明

　　簡述不同版本的各項功能。

### [README-ToC-Generator](https://github.com/DonkeyBear/README-ToC-Generator/tree/main/README-ToC-Generator) `v1.0`

　　功能相對齊全的 README 目錄產生器，可透過 `Config.txt` 設定目錄樣式。

### [Simple-README-ToC-Generator](https://github.com/DonkeyBear/README-ToC-Generator/tree/main/Simple-README-ToC-Generator) `v1.0`

　　精簡的 README 目錄產生器。

　　刪去了透過 `Config.txt` 設定的功能，無須導入自製模組，適合用作修改各種衍生或客製版本。

### [DonkeBearStyle-ToC-Generator](https://github.com/DonkeyBear/README-ToC-Generator/tree/main/DonkeBearStyle-ToC-Generator) `v1.0`

　　依照我的個人使用習慣客製化的版本，基本上我也都是直接使用這個版本產生 README 目錄的。

[返回目錄](#目錄)

## 使用說明

　　將編寫好的 `README.md` 與目錄產生器置於同一路徑下，執行目錄產生器後即自動生成目錄 `ToC.md`。

[返回目錄](#目錄)

