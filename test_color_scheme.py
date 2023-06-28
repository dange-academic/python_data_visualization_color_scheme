import matplotlib.pyplot as plt
import matplotlib.patches as patches


# 蓝色 - 'b' 或 '#0000FF'
# 绿色 - 'g' 或 '#008000'
# 红色 - 'r' 或 '#FF0000'
# 青色 - 'c' 或 '#00FFFF'
# 品红 - 'm' 或 '#FF00FF'
# 黄色 - 'y' 或 '#FFFF00'
# 黑色 - 'k' 或 '#000000'
# 白色 - 'w' 或 '#FFFFFF'
# 橙色 - '#FFA500'
# 紫色 - '#800080'
# 棕色 - '#A52A2A'
# 粉红色 - '#FFC0CB'
# 灰色 - '#808080'
# 金色 - '#FFD700'
# 银色 - '#C0C0C0'
# 深红色 - '#8B0000'
# 深蓝色 - '#00008B'
# 深绿色 - '#006400'
# 深青色 - '#008B8B'
# 深品红色 - '#8B008B'
# 深黄色 - '#FFD700'
# 深灰色 - '#A9A9A9'


# color_codes = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w', '#FFA500',\
# '#800080', '#A52A2A', '#FFC0CB', '#808080', '#FFD700', '#C0C0C0',\
# '#8B0000', '#00008B', '#006400', '#008B8B', '#8B008B', '#FFD700',\
# '#A9A9A9', "#1abc9c", "#2ecc71", "#3498db", "#9b59b6", "#34495e",\
# "#f1c40f", "#e67e22", "#e74c3c", "#dfe4ea", "#95a5a6", "#eccc68",\
# "#ff7f50", "#ff6b81", "#a4b0be", "#57606f", "#7bed9f", "#70a1ff",\
# "#5352ed"]
# print(len(color_codes))


# matplotlib官方颜色
color_codes = ["black", "dimgray", "dimgrey", "gray", "grey", "darkgray", "darkgrey",\
"silver", "lightgray", "lightgrey", "gainsboro", "whitesmoke", "white", "snow", "rosybrown",\
"lightcoral", "indianred", "brown", "firebrick", "maroon", "darkred", "red", "mistyrose",\
"salmon", "tomato", "darksalmon", "coral", "orangered", "lightsalmon", "sienna", "seashell",\
"chocolate", "saddlebrown", "sandybrown", "peachpuff", "peru", "linen", "bisque", "darkorange",\
"burlywood", "antiquewhite", "tan", "navajowhite", "blanchedalmond", "papayawhip", "moccasin",\
"orange", "wheat", "oldlace", "floralwhite", "darkgoldenrod", "goldenrod", "cornsilk", "gold",\
"lemonchiffon", "khaki", "palegoldenrod", "darkkhaki", "ivory", "beige", "lightyellow",\
"lightgoldenrodyellow", "olive", "yellow", "olivedrab", "yellowgreen", "darkolivegreen",\
"greenyellow", "chartreuse", "lawngreen", "honeydew", "darkseagreen", "palegreen", "lightgreen",\
"forestgreen", "limegreen", "darkgreen", "green", "lime", "seagreen", "mediumseagreen", "springgreen",\
"mintcream", "mediumspringgreen", "mediumaquamarine", "aquamarine", "turquoise", "lightseagreen",\
"mediumturquoise", "azure", "lightcyan", "paleturquoise", "darkslategray", "darkslategrey",\
"teal", "darkcyan", "aqua", "cyan", "darkturquoise", "cadetblue", "powderblue", "lightblue",\
"deepskyblue", "skyblue", "lightskyblue", "steelblue", "aliceblue", "dodgerblue", "lightslategray",\
"lightslategrey", "slategray", "slategrey", "lightsteelblue", "cornflowerblue", "royalblue",\
"ghostwhite", "lavender", "midnightblue", "navy", "darkblue", "mediumblue", "blue", "slateblue",\
"darkslateblue", "mediumslateblue", "mediumpurple", "rebeccapurple", "blueviolet", "indigo",\
"darkorchid", "darkviolet", "mediumorchid", "thistle", "plum", "violet", "purple", "darkmagenta",\
"fuchsia", "magenta", "orchid", "mediumvioletred", "deeppink", "hotpink", "lavenderblush",\
"palevioletred", "crimson", "pink", "lightpink"]
print(len(color_codes))



fig, ax = plt.subplots()

c = 0
for i in range(14):
    for j in range(10):
        # 创建一个矩形，宽度和高度都为0.1
        rect = patches.Rectangle((0.1*i, 0.1*j), 0.1, 0.1, facecolor=color_codes[c])
        c += 1

        # 将矩形添加到图表中
        ax.add_patch(rect)
plt.axis('off')  # 隐藏坐标轴
plt.show()
