import module.generator as gi
import argparse
import configparser

def _color(color:str)->str:
    if len(color) == 6:
        return (int(color[0:2],16),int(color[2:4],16),int(color[4:6],16))
    elif len(color)== 3:
        return ( \
                int(color[0:1]+color[0:1],16), \
                int(color[1:2]+color[1:2],16), \
                int(color[2:3]+color[2:3],16) \
                )
    else:
        print('color select eroor')
        exit()

def _show_config(mode, width, height, bc, lc, lw, la, length):
    imput = [mode, width, height, lc, bc, lw, la, length]
    config = configparser.ConfigParser()
    config.read("setting.ini")
    sections = config.sections()

    for i in sections:
        for j, (key, value) in enumerate(config.items(i)):
            if not str(imput[j]) == value:
                print('---- UPDATE CONFIG ----')
                print('> {0}{1}\033[36m{2}->{3}\033[0m'.format(key,' ' * (14- len(key)) ,str(value),str(imput[j])))
                config.set(i, key, str(imput[j]))
                with open('setting.ini', 'w') as file:
                    config.write(file)



    for i in sections:
        print('------- SECTION -------')
        for j, (key, value) in enumerate(config.items(i)):
            print('> {0}{1}\033[36m{2}\033[0m'.format(key,' ' * (14- len(key)) ,str(value)))



    return



def main():
    config = configparser.ConfigParser()
    config.read("setting.ini")
    default_config = "default"



    psr = argparse.ArgumentParser()
    # psr.add_argument('-w', '--word', default='デフォルト値', help="パラメータの説明")
    psr.add_argument('-m', '--mode', default=config.get(default_config, 'mode'), type=str, help="img or text")
    psr.add_argument('-w', '--width', default=int(config.get(default_config, 'width')), type=int, help="image width")
    psr.add_argument('-t', '--tall', default=int(config.get(default_config, 'height')), type=int, help="image height")

    psr.add_argument('-c', '--color', default=config.get(default_config, 'bc_color'), type=str, help="background color")
    psr.add_argument('-lc', '--line_color', default=config.get(default_config, 'line_color'), type=str, help="line color")
    psr.add_argument('-lw', '--line_weight', default=int(config.get(default_config, 'line_weight')), type=str, help="line weight")

    psr.add_argument('-la', '--lang', default=config.get(default_config, 'lang'), type=str, help="text language jp or en")
    psr.add_argument('-len', '--length', default=int(config.get(default_config, 'length')), type=int, help="text length")
    psr.add_argument('-cn', '--config', action='store_true', help="show config and change config")
    # コマンドラインの引数をパースしてargsに入れる．エラーがあったらexitする
    args = psr.parse_args()
    if args.config:
        print('config : ')
        _show_config( \
            args.mode, \
            args.width, \
            args.tall, \
            args.color,  \
            args.line_color, \
            args.line_weight, \
            args.lang, \
            args.length)
        exit()

    color = _color(args.color)
    line_color = _color(args.line_color)

    if args.mode=="img":
        img = gi.GeneratorImg(args.width, args.tall,color)
        img.draw_rectangle(args.line_weight, line_color)
        img.save_img()
    elif args.mode=="text":
        text = gi.TextGenerator(args.length, args.lang)


    else:
        print('mode select eroor')
        exit()


    # print(args.word * args.size)

if __name__ == '__main__':
    main()






# import sys
# import argparse
#
# def get_args():
#     # 準備
#     parser = argparse.ArgumentParser()
#
#     # 標準入力以外の場合
#     if sys.stdin.isatty():
#         parser.add_argument("file", help="please set me", type=str)
#
#     parser.add_argument("--type", type=int)
#     parser.add_argument("--alert", help="optional", action="store_true")
#
#     # 結果を受ける
#     args = parser.parse_args()
#
#     return(args)
#
# def main():
#     args = get_args()
#
#     if hasattr(args, 'file'):
#         print(args.file)
#     print(args.type)
#     print(args.alert)
#
#     if args.alert:
#         None;# alertが設定されている場合
#

#
#  入力
# python dummy.py img 200-300
