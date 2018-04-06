# Git課題

## Gitとは

Gitとはプログラムソースなどのファイルの変更履歴を管理する分散型のバージョン管理システムのことです。

Gitの特徴として、リポジトリと呼ばれる保存領域をローカル環境とリモート環境それぞれに持つことが挙げられます。
開発者それぞれが各々の仕事に集中して作業しやすいため、
主にチーム（プログラマ、デザイナー）で開発するときのバージョン管理に利用されます。

類似のソフトウェアとして、svn(Apache Subversion)があります。
gitとの最大の違いはgitがリポジトリが複数あるのに対して、svnはリポジトリは１つだけです。
これは仕組みとしてシンプルな反面、一人の開発者がコミットするとすべての環境に反映されるため自由なコミットができず、コミットの単位も機能や目的単位ではなくその時点での修正を全て含んだコミットになりがちです。

Gitのメリットには下記のようなものがあり、かつGITHUBが生み出したソーシャルコーディング（みんなで見せ合っていいプログラム作ろうぜ！）
の文化が普及したため現在バージョン管理システムのシェアトップとなっています。

- 大規模開発でのバージョン管理を想定しているため他のバージョン管理システムより高速に動作する。
- ローカルでリポジトリを持つため、オフライン環境下で作業がしやすい。
- 開発者がバラバラに機能別の変更や追加をしても他の人の変更の干渉を一切受けず、それぞれの開発に集中できる。



## git init
`git init`とはカレントディレクトリ上でリポジトリを作成するコマンドです。
コマンドを入力するとgitをそのディレクトリ上で動かすためもろもろの設定が入った
`.git`ディレクトリを作成します。


すでにリポジトリがある状態で`git init`を行うと
`Reinitialized existing Git repository in /Users/kzfm/dive/git-test/.git/`と表示されますが下記の参考urlを見たところ上書きされるわけではなく何も起こりません。
`git branch`や`git log`で確認しましたが今までのブランチや操作が残っていることが確認しています。


> How to undo misoperation of Reinitialized existing Git repository - Stack Overflow http://stackoverflow.com/questions/19397888/how-to-undo-misoperation-of-reinitialized-existing-git-repository


## git add

`git add [filename]`コマンドは変更を確定する前に一旦*ステージング領域*と呼ばれる一時領域にデータを保存します。


`git add .`とすると全ての変更したファイルをステージング領域に保存します。

たとえば `hoge.html` をステージング領域に追加するのは

```git add hoge.html```

になります。

逆に、`hoge.html`をステージング領域に追加されていたとして`hoge.html`をステージング領域から削除するのは
```git reset HEAD hoge.html```になります。

`git reset`コマンドの補足ですが、HEADは省略可能で
ファイルを記載せず単に`git reset`とするとcommit前のステージング領域に乗った全てのファイルの変更を削除します。

補足ですが、
「`git add`なしで`git commit`で一発で変更すればよいのでは？」と思うかもしません。
これに対する回答として「`git add`を挟むことで目的単位のコミットを促す」というメリットが挙げられます。
例えば変更した４つファイルの内３ファイルは機能Aのための改修、残りのファイルはバグBの修正のための変更だとします。
こんな場合でも`commit`しかない場合はえいやと４ファイル分のコミットをしてしまう
一つのコミットにはある目的のための変更をひとかたまりとして扱う方が後から見たときに分かりやすいです。
そのため`git add file1 file2 file3`とした後、
`git diff`で内容を確認し、同じ目的の変更のファイル群として改めて`git commit -m"機能Aの追加改修"`とし、
'git add file4'、`git commit -m "バグBの対応"`
コミット一発では、このような目的単位でコミットを分割するのを忘れがちです。
ステージング領域に乗せて確認するという一手間かけることで目的単位でのコミットすることを確実にします。



## git commit　

`git commit`コマンドはステージング領域に保存された内容をレポジトリに保存するコマンドです。
コミットした内容の履歴は`git　log`コマンドで確認することができます。
コミットした内容を取り消す場合は`git reset HEAD^{n}`でnつ前のコミットに戻ることができます。

例を見てみましょう。
```
commit c4a9f6aad4ea6f5b372b9bc742c1dfc06b8641f1 (HEAD -> master, origin/master, origin/HEAD)
Author: Akihiro Nakao <nakao@diveintocode.jp>
Date:   Wed Mar 21 16:42:30 2018 +0900

    commit message 3

commit cff10b7231c5238cbd7ddab0bc19c3b7f02ba35d
Author: Akihiro Nakao <nakao@diveintocode.jp>
Date:   Wed Mar 21 16:40:31 2018 +0900

    commit message 2

commit 7b6f15fdde0f56dae4541a1a896ef6dca630e28f
Author: Akihiro Nakao <genn777f3@gmail.com>
Date:   Fri Feb 23 19:38:22 2018 +0900

    commit message 1
```

上記のように３つのコミットがある状態で`commit message 1`(2
つ前のコミット)まで戻るためには`git reset HEAD^2`になります。
