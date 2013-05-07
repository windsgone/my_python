# coding: utf-8

print "你进入了一个黑暗的房间，房间有两扇门。选择门1或者门2。"

door = raw_input("> ")

if door == "1":
	print "有只大熊在吃蛋糕，你会如何应对？"
	print "1. 拿起蛋糕"
	print "2. 因为熊而尖叫"

	bear = raw_input("> ")

	if bear == "1":
		print "大熊吃了你的脸！ 干得好！"
	elif bear == "2":
		print "大熊吃了你的腿！ 干得好！"
	else:
		print "好吧，选择 %s 是明智的。 大熊跑了。" % bear		
elif door == "2":
	print "你走入了恶魔邪瞳的无尽深渊中。"
	print "1. 蓝莓"
	print "2. 黄色夹克衣架"
	print "3. 理解左轮手枪的旋律"

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "你活下来了！ 干得好！"
	else:
		print "你疯了！ 干得好！"
else:
	print "你掉到了一把刀上，死了！ 干得好！"
