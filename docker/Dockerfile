FROM postgres:latest

# 日本語ロケールのインストール
RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
    && localedef -i ja_JP -c -f UTF-8 -A /usr/share/locale/locale.alias ja_JP.UTF-8

# タイムゾーンファイルを設定
RUN echo "Asia/Tokyo" > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata

# 環境変数でロケールを設定
ENV LANG ja_JP.utf8

# タイムゾーンを設定
ENV TZ=Asia/Tokyo

# ローカルの設定ファイルをイメージに追加
COPY ./postgresql.conf /etc/postgresql/postgresql.conf
RUN chown postgres:postgres /etc/postgresql/postgresql.conf
RUN chmod 0600 /etc/postgresql/postgresql.conf
