"""Built-in events for the first year of study abroad in Japan."""

from __future__ import annotations

from .models import Choice, Event

EVENTS: tuple[Event, ...] = (
    Event(
        1,
        "区役所で最初の手続き",
        "市役所・区役所",
        "来日した翌日、転入届や健康保険の手続きをすることになりました。窓口では知らない言葉が次々に出てきます。",
        (
            Choice("分からない言葉を職員に聞く", {"japanese": 3, "adaptation": 5, "relationships": 1, "stress": -2}, "分からないことを確認しながら手続きを進めました。"),
            Choice("分かったふりをして進める", {"adaptation": -2, "stress": 6}, "その場は終わりましたが、後で必要書類が足りないことに気づきました。"),
            Choice("翻訳アプリを使って確認する", {"japanese": 1, "adaptation": 3, "stress": -1}, "スマホを使いながら、必要な情報を一つずつ確認できました。"),
        ),
    ),
    Event(
        2,
        "初めてのゼミ",
        "大学",
        "授業のスピードが想像より速く、先生から突然意見を聞かれました。",
        (
            Choice("勇気を出して日本語で答える", {"japanese": 3, "academics": 4, "relationships": 2, "stress": 2}, "完璧ではありませんでしたが、自分の意見を伝えられました。"),
            Choice("授業後に復習して先生に質問する", {"japanese": 2, "academics": 5, "stress": 1}, "授業後に整理したことで、内容への理解が深まりました。"),
            Choice("今日は無理せず聞くだけにする", {"health": 2, "academics": -3, "stress": -2}, "気持ちは楽になりましたが、理解できない部分が少し残りました。"),
        ),
    ),
    Event(
        3,
        "アルバイトを探す",
        "駅前",
        "生活費を考えるとアルバイトも必要です。求人を見ながら、学業とのバランスを考えます。",
        (
            Choice("接客のアルバイトを始める", {"money": 10, "japanese": 4, "health": -3, "academics": -2, "stress": 4}, "接客は大変ですが、日本語を使う機会が一気に増えました。"),
            Choice("大学のTA・学内バイトを探す", {"money": 6, "academics": 2, "japanese": 2, "stress": 1}, "収入は多くありませんが、学業との両立はしやすそうです。"),
            Choice("今学期は勉強を優先する", {"academics": 4, "money": -5, "health": 2, "stress": -1}, "時間には余裕ができましたが、生活費には少し不安が残ります。"),
        ),
    ),
    Event(
        4,
        "期末試験",
        "図書館",
        "試験とレポートの締切が重なりました。残された時間をどう使うか決めなければなりません。",
        (
            Choice("徹夜して全部終わらせる", {"academics": 8, "health": -6, "stress": 8}, "課題は進みましたが、かなり疲れが残りました。"),
            Choice("優先順位を決めて計画的に進める", {"academics": 6, "health": -1, "stress": 2, "adaptation": 2}, "すべてを完璧にはできなくても、落ち着いて締切を守れました。"),
            Choice("一度休んでから最低限を仕上げる", {"academics": -2, "health": 4, "stress": -4}, "成績面では少し妥協しましたが、体調は回復しました。"),
        ),
    ),
    Event(
        5,
        "夏休みの過ごし方",
        "夏休み",
        "長い休みが始まりました。旅行、アルバイト、勉強のどれを優先するか迷います。",
        (
            Choice("日本国内を旅行する", {"money": -8, "adaptation": 6, "relationships": 5, "health": 3, "stress": -3}, "知らない地域を訪れ、日本での生活が少し身近になりました。"),
            Choice("アルバイトを増やす", {"money": 12, "japanese": 4, "health": -3, "stress": 4}, "貯金は増えましたが、休みらしい休みはあまりありませんでした。"),
            Choice("日本語と研究を進める", {"academics": 5, "japanese": 3, "relationships": -1, "stress": 2}, "まとまった時間を使って、学習を進めることができました。"),
        ),
    ),
    Event(
        6,
        "友人からの誘い",
        "大学近くの店",
        "クラスメートから食事に誘われました。翌日は朝から予定があります。",
        (
            Choice("みんなと食事に行く", {"relationships": 8, "japanese": 3, "money": -4, "adaptation": 3, "stress": -2}, "授業では話せなかったことまで話し、友人との距離が縮まりました。"),
            Choice("少人数で短時間だけ参加する", {"relationships": 5, "japanese": 2, "money": -2, "stress": -1}, "無理をしすぎず、人間関係も少し広がりました。"),
            Choice("今日は家で休む", {"health": 3, "relationships": -2, "stress": -2}, "しっかり休めましたが、少しだけ寂しさも感じました。"),
        ),
    ),
    Event(
        7,
        "体調を崩した日",
        "クリニック",
        "朝から熱があり、病院に行くか迷っています。日本の医療機関を一人で利用した経験はありません。",
        (
            Choice("一人でクリニックに行く", {"adaptation": 6, "japanese": 3, "money": -3, "health": 5, "stress": 1}, "受付から診察まで自分で対応し、生活への自信が少しつきました。"),
            Choice("友人に相談して一緒に行ってもらう", {"relationships": 4, "adaptation": 4, "money": -3, "health": 5, "stress": -2}, "助けてもらいながら、受診の流れを理解できました。"),
            Choice("もう少し様子を見る", {"health": -6, "stress": 5}, "休めば治ると思いましたが、体調はさらに悪くなってしまいました。"),
        ),
    ),
    Event(
        8,
        "文化の違いで気まずくなる",
        "研究室",
        "何気ない一言が相手にうまく伝わらず、少し気まずい雰囲気になりました。",
        (
            Choice("相手に直接確認して話し合う", {"japanese": 4, "relationships": 4, "adaptation": 5, "stress": -1}, "言葉だけでなく、伝え方の違いにも気づくことができました。"),
            Choice("何も言わず時間が解決するのを待つ", {"relationships": -3, "stress": 2}, "大きな問題にはなりませんでしたが、少し距離が残りました。"),
            Choice("日本のコミュニケーションについて調べる", {"academics": 2, "adaptation": 4, "stress": -1}, "背景を知ることで、次からどう対応すればよいか見えてきました。"),
        ),
    ),
    Event(
        9,
        "冬の生活費",
        "自宅",
        "光熱費や年末の出費が増え、残高が思ったより少なくなっています。",
        (
            Choice("家計を見直して予算を作る", {"money": 7, "adaptation": 3, "stress": -1}, "支出を整理すると、無理なく削れる部分が見つかりました。"),
            Choice("アルバイトのシフトを増やす", {"money": 11, "health": -5, "academics": -2, "stress": 5}, "収入は増えましたが、授業との両立が少し苦しくなりました。"),
            Choice("家族に一時的に助けてもらう", {"money": 8, "adaptation": -1, "stress": -3}, "すぐに困ることは避けられましたが、自分でも家計を考える必要があります。"),
        ),
    ),
    Event(
        10,
        "研究が進まない",
        "大学院研究室",
        "研究テーマは決まったものの、分析がうまく進まず焦りを感じています。",
        (
            Choice("指導教員に早めに相談する", {"academics": 7, "japanese": 2, "relationships": 2, "stress": -1}, "相談したことで問題点が整理され、次の一歩が見えました。"),
            Choice("まず自分で徹底的に調べる", {"academics": 5, "stress": 4}, "理解は深まりましたが、一人で抱え込む時間も長くなりました。"),
            Choice("いったん別の作業を進める", {"health": 2, "academics": -3, "stress": -2}, "気分転換にはなりましたが、研究課題はまだ残っています。"),
        ),
    ),
    Event(
        11,
        "これからの進路",
        "キャリアセンター",
        "日本で就職するか、進学するか、帰国するか。そろそろ将来を具体的に考える時期になりました。",
        (
            Choice("日本企業の説明会に参加する", {"japanese": 4, "adaptation": 5, "relationships": 3, "stress": 3}, "実際に話を聞くことで、日本で働くイメージが具体的になりました。"),
            Choice("研究を優先して進学情報を集める", {"academics": 6, "japanese": 2, "stress": 1}, "将来の研究生活について考える時間が増えました。"),
            Choice("まだ決めず、生活を整える", {"health": 4, "stress": -4, "adaptation": 1}, "結論は先送りしましたが、落ち着いて考える余裕ができました。"),
        ),
    ),
    Event(
        12,
        "日本での一年を振り返る",
        "桜の季節",
        "来日から一年。最初は分からないことだらけだった生活を振り返ります。",
        (
            Choice("一年の経験を日本語で発表する", {"japanese": 4, "academics": 4, "adaptation": 4, "stress": -2}, "自分の成長を言葉にすることで、一年間の変化を実感できました。"),
            Choice("友人と一年を祝う", {"relationships": 6, "health": 3, "money": -3, "stress": -4}, "周りの人とのつながりが、この一年を支えてくれたことに気づきました。"),
            Choice("次年度の目標を立てて勉強する", {"academics": 5, "japanese": 3, "health": -2, "stress": 2}, "次の一年に向けて、すぐに新しい目標を立てました。"),
        ),
    ),
)


def get_event(month: int) -> Event:
    """Return the event for a month between 1 and 12."""
    if not 1 <= month <= len(EVENTS):
        raise ValueError("month must be between 1 and 12")
    return EVENTS[month - 1]
