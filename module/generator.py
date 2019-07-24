import cv2
import numpy as np
import random
import os

class GeneratorImg(object):
    """GeneratorImg

    """

    def __init__(self, width, height, bg_color=(255, 255, 255)):
        super(GeneratorImg, self).__init__()
        self.width = width
        self.height = height
        # Since OpenCV uses BGR, convert the color first
        self.bg_color = tuple(reversed(bg_color))

        self.create_blank()


    def create_blank(self)->object:
        """Create new image(numpy array) filled with certain color in RGB"""
        # Create black blank image
        self.img = np.zeros((self.height, self.width, 3), np.uint8)
        # Fill image with color
        self.img[:] = self.bg_color#
        # return self.img

    def draw_rectangle(self, waight,line_color)->object:
        """矩形を描画"""
        line_color = tuple(reversed(line_color))
        self.img = cv2.rectangle(self.img, (0,0), (self.width-1, self.height-1), line_color, waight)
        self.img = cv2.line(self.img, (0,0), (self.width, self.height), line_color, waight)
        self.img = cv2.line(self.img, (self.width,0), (0, self.height), line_color, waight)

    def save_img(self):
        try:
            file_name = '{0}_{1}.png'.format(self.width, self.height)
            cv2.imwrite(file_name, self.img)
            print('Image Link (Command & double click)')
            print(' > \033[36mfile:///{}\033[0m'.format(os.path.abspath(file_name)))
        except:
            print('save error')


    def draw_img(self):
        cv2.imshow("Blank Image", self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


class TextGenerator(object):
    """TextGenerator
        text max length : 1500
    """

    def __init__(self, textlen,lang="ja"):
        super(TextGenerator, self).__init__()
        self.textlen = textlen
        self.lang = lang
        if lang=="en":
            self.en_text = [self.en_UndertheSea,self.en_gullivers_travels,self.en_alice]
            self.document_shuffle(self.en_text)
        elif lang=="ja":
            self.ja_text = [self.ja_kokoro,self.ja_kumonoito,self.ja_lemon]
            self.document_shuffle(self.ja_text)



    def document_shuffle(self, funcArr):
        # print(int(random.random()*3)
        self.text = funcArr[int(random.random()*3)]()
        print(self.text)
        os.system("echo '%s' | pbcopy" % self.text)
        print(' > \033[36mCopy in Clipbord!\033[0m')

    def ja_kokoro(self):
        """夏目漱石 - こころ
             REFERENCE :
                青空文庫
                https://www.aozora.gr.jp/cards/000148/files/773_14560.html
        """

        text = "私わたくしはその人を常に先生と呼んでいた。だからここでもただ先生と書くだけで本名は打ち明けない。これは世間を憚はばかる遠慮というよりも、その方が私にとって自然だからである。私はその人の記憶を呼び起すごとに、すぐ「先生」といいたくなる。筆を執とっても心持は同じ事である。よそよそしい頭文字かしらもじなどはとても使う気にならない。私が先生と知り合いになったのは鎌倉かまくらである。その時私はまだ若々しい書生であった。暑中休暇を利用して海水浴に行った友達からぜひ来いという端書はがきを受け取ったので、私は多少の金を工面くめんして、出掛ける事にした。私は金の工面に二に、三日さんちを費やした。ところが私が鎌倉に着いて三日と経たたないうちに、私を呼び寄せた友達は、急に国元から帰れという電報を受け取った。電報には母が病気だからと断ってあったけれども友達はそれを信じなかった。友達はかねてから国元にいる親たちに勧すすまない結婚を強しいられていた。彼は現代の習慣からいうと結婚するにはあまり年が若過ぎた。それに肝心かんじんの当人が気に入らなかった。それで夏休みに当然帰るべきところを、わざと避けて東京の近くで遊んでいたのである。彼は電報を私に見せてどうしようと相談をした。私にはどうしていいか分らなかった。けれども実際彼の母が病気であるとすれば彼は固もとより帰るべきはずであった。それで彼はとうとう帰る事になった。せっかく来た私は一人取り残された。学校の授業が始まるにはまだ大分だいぶ日数ひかずがあるので鎌倉におってもよし、帰ってもよいという境遇にいた私は、当分元の宿に留とまる覚悟をした。友達は中国のある資産家の息子むすこで金に不自由のない男であったけれども、学校が学校なのと年が年なので、生活の程度は私とそう変りもしなかった。したがって一人ひとりぼっちになった私は別に恰好かっこうな宿を探す面倒ももたなかったのである。宿は鎌倉でも辺鄙へんぴな方角にあった。玉突たまつきだのアイスクリームだのというハイカラなものには長い畷なわてを一つ越さなければ手が届かなかった。車で行っても二十銭は取られた。けれども個人の別荘はそこここにいくつでも建てられていた。それに海へはごく近いので海水浴をやるには至極便利な地位を占めていた。私は毎日海へはいりに出掛けた。古い燻くすぶり返った藁葺わらぶきの間あいだを通り抜けて磯いそへ下りると、この辺へんにこれほどの都会人種が住んでいるかと思うほど、避暑に来た男や女で砂の上が動いていた。ある時は海の中が銭湯せんとうのように黒い頭でごちゃごちゃしている事もあった。その中に知った人を一人ももたない私も、こういう賑にぎやかな景色の中に裹つつまれて、砂の上に寝ねそべってみたり、膝頭ひざがしらを波に打たしてそこいらを跳はね廻まわるのは愉快であった。私は実に先生をこの雑沓ざっとうの間あいだに見付け出したのである。その時海岸には掛茶屋かけぢゃやが二軒あった。私はふとした機会はずみからその一軒の方に行き慣なれていた。長谷辺はせへんに大きな別荘を構えている人と違って、各自めいめいに専有の着換場きがえばを拵こしらえていないここいらの避暑客には、ぜひともこうした共同着換所といった風ふうなものが必要なのであった。彼らはここで茶を飲み、ここで休息する外ほかに、ここで海水着を洗濯させたり、ここで鹹しおはゆい身体からだを清めたり、ここへ帽子や傘かさを預けたりするのである。海水着を持たない私にも持物を盗まれる恐れはあったので、私は海へはいるたびにその茶屋へ一切いっさいを脱ぬぎ棄すてる事にしていた。"

        return text[0:self.textlen]


    def ja_kumonoito(self):
        """芥川龍之介 - 蜘蛛の糸
             REFERENCE :
                青空文庫
                https://www.aozora.gr.jp/cards/000879/files/92_14545.html
        """
        text = "ある日の事でございます。御釈迦様おしゃかさまは極楽の蓮池はすいけのふちを、独りでぶらぶら御歩きになっていらっしゃいました。池の中に咲いている蓮はすの花は、みんな玉のようにまっ白で、そのまん中にある金色きんいろの蕊ずいからは、何とも云えない好よい匂においが、絶間たえまなくあたりへ溢あふれて居ります。極楽は丁度朝なのでございましょう。やがて御釈迦様はその池のふちに御佇おたたずみになって、水の面おもてを蔽おおっている蓮の葉の間から、ふと下の容子ようすを御覧になりました。この極楽の蓮池の下は、丁度地獄じごくの底に当って居りますから、水晶すいしようのような水を透き徹して、三途さんずの河や針の山の景色が、丁度覗のぞき眼鏡めがねを見るように、はっきりと見えるのでございます。するとその地獄の底に、カンダタかんだたと云う男が一人、ほかの罪人と一しょに蠢うごめいている姿が、御眼に止まりました。このカンダタと云う男は、人を殺したり家に火をつけたり、いろいろ悪事を働いた大泥坊でございますが、それでもたった一つ、善い事を致した覚えがございます。と申しますのは、ある時この男が深い林の中を通りますと、小さな蜘蛛くもが一匹、路ばたを這はって行くのが見えました。そこでカンダタは早速足を挙げて、踏み殺そうと致しましたが、「いや、いや、これも小さいながら、命のあるものに違いない。その命を無暗むやみにとると云う事は、いくら何でも可哀そうだ。」と、こう急に思い返して、とうとうその蜘蛛を殺さずに助けてやったからでございます。御釈迦様は地獄の容子を御覧になりながら、このカンダタには蜘蛛を助けた事があるのを御思い出しになりました。そうしてそれだけの善い事をした報むくいには、出来るなら、この男を地獄から救い出してやろうと御考えになりました。幸い、側を見ますと、翡翠ひすいのような色をした蓮の葉の上に、極楽の蜘蛛が一匹、美しい銀色の糸をかけて居ります。御釈迦様はその蜘蛛の糸をそっと御手に御取りになって、玉のような白蓮しらはすの間から、遥か下にある地獄の底へ、まっすぐにそれを御下おろしなさいました。こちらは地獄の底の血の池で、ほかの罪人と一しょに、浮いたり沈んだりしていたカンダタかんだたでございます。何しろどちらを見ても、まっ暗で、たまにそのくら暗からぼんやり浮き上っているものがあると思いますと、それは恐しい針の山の針が光るのでございますから、その心細さと云ったらございません。その上あたりは墓の中のようにしんと静まり返って、たまに聞えるものと云っては、ただ罪人がつく微かすかな嘆息たんそくばかりでございます。これはここへ落ちて来るほどの人間は、もうさまざまな地獄の責苦せめくに疲れはてて、泣声を出す力さえなくなっているのでございましょう。ですからさすが大泥坊のカンダタも、やはり血の池の血に咽むせびながら、まるで死にかかった蛙かわずのように、ただもがいてばかり居りました。ところがある時の事でございます。何気なにげなくカンダタが頭を挙げて、血の池の空を眺めますと、そのひっそりとした暗の中を、遠い遠い天上から、銀色の蜘蛛くもの糸が、まるで人目にかかるのを恐れるように、一すじ細く光りながら、するすると自分の上へ垂れて参るのではございませんか。カンダタはこれを見ると、思わず手を拍うって喜びました。この糸に縋すがりついて、どこまでものぼって行けば、きっと地獄からぬけ出せるのに相違ございません。いや、うまく行くと、極楽へはいる事さえも出来ましょう。そうすれば、もう針の山へ追い上げられる事もなくなれば、血の池に沈められる事もある筈はございません。こう思いましたからカンダタかんだたは、早速その蜘蛛の糸を両手でしっかりとつかみながら、一生懸命に上へ上へとたぐりのぼり始めました。元より大泥坊の事でございますから、こう云う事には昔から、慣れ切っているのでございます。"

        return text[0:self.textlen]

    def ja_lemon(self):
        """梶井基次郎 - 檸檬
             REFERENCE :
                青空文庫
                https://www.aozora.gr.jp/cards/000074/files/424_19826.html
        """
        text = "えたいの知れない不吉な塊が私の心を始終圧おさえつけていた。焦躁しょうそうと言おうか、嫌悪と言おうか――酒を飲んだあとに宿酔ふつかよいがあるように、酒を毎日飲んでいると宿酔に相当した時期がやって来る。それが来たのだ。これはちょっといけなかった。結果した肺尖はいせんカタルや神経衰弱がいけないのではない。また背を焼くような借金などがいけないのではない。いけないのはその不吉な塊だ。以前私を喜ばせたどんな美しい音楽も、どんな美しい詩の一節も辛抱がならなくなった。蓄音器を聴かせてもらいにわざわざ出かけて行っても、最初の二三小節で不意に立ち上がってしまいたくなる。何かが私を居堪いたたまらずさせるのだ。それで始終私は街から街を浮浪し続けていた。何故なぜだかその頃私は見すぼらしくて美しいものに強くひきつけられたのを覚えている。風景にしても壊れかかった街だとか、その街にしてもよそよそしい表通りよりもどこか親しみのある、汚い洗濯物が干してあったりがらくたが転がしてあったりむさくるしい部屋が覗のぞいていたりする裏通りが好きであった。雨や風が蝕むしばんでやがて土に帰ってしまう、と言ったような趣きのある街で、土塀どべいが崩れていたり家並が傾きかかっていたり――勢いのいいのは植物だけで、時とするとびっくりさせるような向日葵ひまわりがあったりカンナが咲いていたりする。時どき私はそんな路を歩きながら、ふと、そこが京都ではなくて京都から何百里も離れた仙台とか長崎とか――そのような市へ今自分が来ているのだ――という錯覚を起こそうと努める。私は、できることなら京都から逃げ出して誰一人知らないような市へ行ってしまいたかった。第一に安静。がらんとした旅館の一室。清浄な蒲団ふとん。匂においのいい蚊帳かやと糊のりのよくきいた浴衣ゆかた。そこで一月ほど何も思わず横になりたい。希ねがわくはここがいつの間にかその市になっているのだったら。――錯覚がようやく成功しはじめると私はそれからそれへ想像の絵具を塗りつけてゆく。なんのことはない、私の錯覚と壊れかかった街との二重写しである。そして私はその中に現実の私自身を見失うのを楽しんだ。私はまたあの花火というやつが好きになった。花火そのものは第二段として、あの安っぽい絵具で赤や紫や黄や青や、さまざまの縞模様しまもようを持った花火の束、中山寺の星下り、花合戦、枯れすすき。それから鼠花火ねずみはなびというのは一つずつ輪になっていて箱に詰めてある。そんなものが変に私の心を唆そそった。それからまた、びいどろという色硝子ガラスで鯛や花を打ち出してあるおはじきが好きになったし、南京玉なんきんだまが好きになった。またそれを嘗なめてみるのが私にとってなんともいえない享楽だったのだ。あのびいどろの味ほど幽かすかな涼しい味があるものか。私は幼い時よくそれを口に入れては父母に叱られたものだが、その幼時のあまい記憶が大きくなって落ち魄ぶれた私に蘇よみがえってくる故せいだろうか、まったくあの味には幽かすかな爽さわやかななんとなく詩美と言ったような味覚が漂って来る。察しはつくだろうが私にはまるで金がなかった。とは言えそんなものを見て少しでも心の動きかけた時の私自身を慰めるためには贅沢ぜいたくということが必要であった。二銭や三銭のもの――と言って贅沢なもの。美しいもの――と言って無気力な私の触角にむしろ媚こびて来るもの。――そう言ったものが自然私を慰めるのだ。生活がまだ蝕むしばまれていなかった以前私の好きであった所は、たとえば丸善であった。赤や黄のオードコロンやオードキニン。洒落しゃれた切子細工や典雅なロココ趣味の浮模様を持った琥珀色や翡翠色ひすいいろの香水壜こうすいびん。煙管きせる、小刀、石鹸せっけん、煙草たばこ。私はそんなものを見るのに小一時間も費すことがあった。そして結局一等いい鉛筆を一本買うくらいの贅沢をするのだった。しかしここももうその頃の私にとっては重くるしい場所に過ぎなかった。書籍、学生、勘定台、これらはみな借金取りの亡霊のように私には見えるのだった。"

        return text[0:self.textlen]

    def en_UndertheSea(self):
        """Jules Verne - Twenty Thousand Leagues Under the Sea
             REFERENCE :
                Project Gutenberg
                http://www.gutenberg.org/ebooks/2488
        """
        text = "THE YEAR 1866 was marked by a bizarre development, an unexplained and downright inexplicable phenomenon that surely no one has forgotten. Without getting into those rumors that upset civilians in the seaports and deranged the public mind even far inland, it must be said that professional seamen were especially alarmed. Traders, shipowners, captains of vessels, skippers, and master mariners from Europe and America, naval officers from every country, and at their heels the various national governments on these two continents, were all extremely disturbed by the business. In essence, over a period of time several ships had encountered “an enormous thing” at sea, a long spindle-shaped object, sometimes giving off a phosphorescent glow, infinitely bigger and faster than any whale. The relevant data on this apparition, as recorded in various logbooks, agreed pretty closely as to the structure of the object or creature in question, its unprecedented speed of movement, its startling locomotive power, and the unique vitality with which it seemed to be gifted. If it was a cetacean, it exceeded in bulk any whale previously classified by science. No naturalist, neither Cuvier nor Lacépède, neither Professor Dumeril nor Professor de Quatrefages, would have accepted the existence of such a monster sight unseen—specifically, unseen by their own scientific eyes. Striking an average of observations taken at different times—rejecting those timid estimates that gave the object a length of 200 feet, and ignoring those exaggerated views that saw it as a mile wide and three long—you could still assert that this phenomenal creature greatly exceeded the dimensions of anything then known to ichthyologists, if it existed at all. "
        return text[0:self.textlen]

    def en_gullivers_travels(self):
        """Jonathan Swift - GULLIVER’S TRAVELS
             REFERENCE :
                Project Gutenberg
                http://www.gutenberg.org/ebooks/829
        """
        text = "My father had a small estate in Nottinghamshire: I was the third of five sons.  He sent me to Emanuel College in Cambridge at fourteen years old, where I resided three years, and applied myself close to my studies; but the charge of maintaining me, although I had a very scanty allowance, being too great for a narrow fortune, I was bound apprentice to Mr. James Bates, an eminent surgeon in London, with whom I continued four years.  My father now and then sending me small sums of money, I laid them out in learning navigation, and other parts of the mathematics, useful to those who intend to travel, as I always believed it would be, some time or other, my fortune to do.  When I left Mr. Bates, I went down to my father: where, by the assistance of him and my uncle John, and some other relations, I got forty pounds, and a promise of thirty pounds a year to maintain me at Leyden: there I studied physic two years and seven months, knowing it would be useful in long voyages. Soon after my return from Leyden, I was recommended by my good master, Mr. Bates, to be surgeon to the Swallow, Captain Abraham Pannel, commander; with whom I continued three years and a half, making a voyage or two into the Levant, and some other parts.  When I came back I resolved to settle in London; to which Mr. Bates, my master, encouraged me, and by him I was recommended to several patients.  I took part of a small house in the Old Jewry; and being advised to alter my condition, I married Mrs. Mary Burton, second daughter to Mr. Edmund Burton, hosier, in Newgate-street, with whom I received four hundred pounds for a portion."

        return text[0:self.textlen]

    def en_alice(self):
        """Lewis Carroll - Alice's Adventures in Wonderland
             REFERENCE :
                Project Gutenberg
                http://www.gutenberg.org/ebooks/28885
        """
        text ='ALICE was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice, "without pictures or conversations?"  So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid) whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.  There was nothing so _very_ remarkable in that; nor did Alice think it so _very_ much out of the way to hear the Rabbit say to itself, "Oh dear! Oh dear! I shall be too late!" (when she thought it over afterwards, it occurred to her that she ought to have wondered at this, but at the time it all seemed quite natural); but when the Rabbit actually _took a watch out of its waistcoat-pocket_, and looked at it, and then hurried on, Alice started to her feet, for it flashed across her mind that she had never before seen a rabbit with either a waistcoat-pocket, or a watch to take out of it, and burning with curiosity, she ran across the field after it, and was just in time to see it pop down a large rabbit-hole under the hedge.  In another moment down went Alice after it, never once considering how in the world she was to get out again.  The rabbit-hole went straight on like a tunnel for some way, and then dipped suddenly down, so suddenly that Alice had not a moment to think about stopping herself before she found herself falling down what seemed to be a very deep well.'

        return text[0:self.textlen]

#
# help(TextGenerator)
