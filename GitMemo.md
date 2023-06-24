# Git学習
## Gitコマンド

    ローカルリポジトリの作成
        git init

    状態の確認
        git status

    ファイルを登録
        git add

    ファイルを直前のコミットの状態に戻す
        git checkout -- GitMemo.md

    git管理下のファイルを削除する↓＋コミット
        git rm  GitMemo.md

    sshキー生成
        ssh-keygen -t ed25519 -C "nainaidaidai07@gmail.com"
    
    sshコピー、ペーストは shift+Insert
        clip < /c/Users/naitodaichi/.ssh/id_ed25519.pub

    カレントディレクトリをエクスプローラーで開く
        start .

##  Github使い方

    リポジトリ複製
        フォークコマンド

    リポジトリ作成
        +/New repository

    ローカルリポジトリ内にコピーフォルダを取得、""内はcode内のsshをコピー
        git clone ""
    
    クローン元の確認
        git remote -v

## ブランチについて
    ブランチを移動すればvscodeの情報も変わる

    ブランチ作成、確認、移動
        git branch update-venue
        git branch
        git checkout update-venue

    まとめて
        git checkout -b speakers-info

    別ブランチと比較
        git diff master

    マージした後削除
        git branch -d speakers-info
    
    プッシュ
        git push origin speakers-info
    
    プル（マスターブランチに移動）
        git pull origin master

    マージ（speakers-infoブランチに移動）
        git merge master