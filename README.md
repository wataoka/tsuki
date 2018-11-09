# 月の絵文字で絵を描く

このプログラムを使えば月の絵文字で絵を描くことができます。

## 必要なインストール
- numpy
- emoji
- pillow

全部下のようにpipでinstallできますが、各自しっかり調べてください。

```command
pip install numpy
pip install emoji
pip install pillow
```

## 使い方
1. このリポジトリをクローンしてください。
2. ターミナルから`python main.py`を実行してください。

おそらく下のようにリンゴマークが現れるかと思います。

![terminal](https://github.com/wataoka/tsuki/blob/master/images/terminal.png)

## パラメータ
このプログラムではコマンドライン引数を与えることができます。  

コマンドライン引数の種類は以下です。

|引数|説明|
|:--|:--|
|path|画像のパス|
|col|月の横の列の数|

### 例

```command
python main.py --path ./images/他の画像の名前
```

```command
python main.py --path ./images/他の画像の名前 --col 20
```

## アルゴリズム解説記事
- [月で絵を描きたいだと？それならpythonに任せなさい](https://qiita.com/wataoka/items/261fc12c956a517049d8#7-5%E3%81%A86%E3%82%92%E7%94%BB%E5%83%8F%E3%81%AE%E9%9A%85%E3%80%85%E3%81%AB%E3%82%8F%E3%81%9F%E3%82%8B%E3%81%BE%E3%81%A7%E7%B9%B0%E3%82%8A%E8%BF%94%E3%81%99)

## 月文字ジェネレータ
- [月文字ジェネレータ](https://tsukimoji.com/)
- [解説記事](https://qiita.com/Yougurut)

## 自己紹介

冒頭に書くと邪魔になるので最後にひっそりと自己紹介させてください。

<img src="https://qiita-image-store.s3.amazonaws.com/0/221435/16727490-2b41-4318-cc25-e2601479e77a.jpeg" width=30%>

|名前|綿岡晃輝|
|:--|:--|
|職業|大学4年生|
|分野|機械学習, 深層学習, 音声処理|
|Twitter|[@Wataoka_Koki](https://twitter.com/Wataoka_Koki)|


<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">月で安倍晋三作った <a href="https://t.co/4ohnJtNzTk">pic.twitter.com/4ohnJtNzTk</a></p>&mdash; 綿岡晃輝 (@koki_wataoka) <a href="https://twitter.com/koki_wataoka/status/1007151811692670976?ref_src=twsrc%5Etfw">2018年6月14日</a></blockquote>
