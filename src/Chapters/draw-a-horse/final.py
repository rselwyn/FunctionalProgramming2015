#final`


from graphics import *


win = GraphWin("KUSZZZZZZZZZZZZ FINAL",600,600)
horse = Polygon(Point(125,207),Point(173,304),Point(414,284),Point(375,195),Point(380,179),Point(385,173),Point(395,177),Point(404,177),Point(410,179),Point(414,179),Point(423,184),Point(432,177),Point(435,172),Point(437,166),Point(437,155),Point(436,152),Point(426,149),Point(418,143),Point(418,143),Point(408,143),Point(404,142),Point(392,139),Point(385,133),Point(380,127),Point(379,121),Point(369,120),Point(369,120),Point(366,128),Point(368,134),Point(369,138),Point(369,143),Point(361,143),Point(354,143),Point(352,144),Point(351,138),Point(348,133),Point(346,133),Point(342,130),Point(336,130),Point(334,141),Point(334,141),Point(334,150),Point(338,152),Point(341,153),Point(336,156),Point(336,161),Point(328,170),Point(325,173),Point(313,194),Point(280,202),Point(253,204),Point(176,208),Point(145,205))
horse.setFill("grey")
horse.draw(win)
tail = Polygon(Point(126,207),Point(112,208),Point(101,215),Point(99,219),Point(90,225),Point(84,229),Point(80,238),Point(68,250),Point(65,264),Point(67,266),Point(68,266),Point(69,266),Point(70,266),Point(74,262),Point(79,256),Point(79,255),Point(79,265),Point(78,266),Point(74,274),Point(74,277),Point(82,273),Point(90,267),Point(90,264),Point(90,264),Point(91,266),Point(91,268),Point(91,274),Point(92,290),Point(104,289),Point(104,286),Point(104,282),Point(104,269),Point(112,270),Point(112,275),Point(115,282),Point(123,283),Point(125,280),Point(123,268),Point(114,251),Point(112,246),Point(110,227),Point(110,226),Point(116,219),Point(119,212),Point(122,210),Point(126,207),Point(116,203))
tail.setFill("black")
tail.draw(win)

leg1 = Polygon(Point(185,269),Point(200,261),Point(212,268),Point(212,275),Point(219,277),Point(223,286),Point(227,293),Point(229,295),Point(233,298),Point(236,300),Point(246,317),Point(256,324),Point(248,337),Point(237,347),Point(220,358),Point(219,359),Point(203,376),Point(189,382),Point(179,398),Point(152,381),Point(160,375),Point(166,371),Point(174,368),Point(177,364),Point(177,361),Point(185,352),Point(196,346),Point(197,340),Point(200,339),Point(218,324),Point(210,312),Point(206,302),Point(201,295),Point(201,294),Point(195,287),Point(185,268))
leg1.setFill("grey")
leg1.draw(win)

leg2 = Polygon(Point(230,287),Point(259,282),Point(270,302),Point(270,316),Point(270,347),Point(271,353),Point(270,380),Point(270,391),Point(263,409),Point(240,402),Point(241,392),Point(252,379),Point(252,361),Point(252,349),Point(252,335),Point(252,326),Point(234,296))
leg2.setFill("grey")
leg2.draw(win)

leg4 = Polygon(Point(373,271),Point(393,257),Point(466,326),Point(389,397),Point(355,383),Point(427,324),Point(375,272))
leg4.setFill("grey")
leg4.draw(win)
leg3 = Polygon(Point(324,251),Point(344,239),Point(351,247),Point(354,249),Point(356,259),Point(367,260),Point(368,271),Point(377,271),Point(381,286),Point(382,288),Point(385,296),Point(390,305),Point(389,310),Point(389,319),Point(389,326),Point(391,339),Point(394,356),Point(394,363),Point(392,372),Point(396,382),Point(396,388),Point(397,398),Point(396,403),Point(396,408),Point(375,410),Point(366,316),Point(325,254))
leg3.setFill("grey")
leg3.draw(win)

body = Rectangle(Point(173,85),Point(235,195))
body.setFill("black")
body.draw(win)

body = Rectangle(Point(173,197),Point(256,222))
body.setFill("black")
body.draw(win)

head = Circle(Point(200,52),30)
head.setFill("black")
head.draw(win)
nextLeg = Rectangle(Point(228,227),Point(256,264))
nextLeg.setFill("black")
nextLeg.draw(win)

n = Rectangle(Point(228,270),Point(281,296))
n.setFill("black")
n.draw(win)

arm1 = Polygon(Point(194,111),Point(252,136),Point(293,142),Point(293,125),Point(252,118),Point(224,106))
arm1.setFill("black")
arm1.draw(win)

arm2 = Polygon(Point(231,104),Point(282,96),Point(285,113),Point(226,116))
arm2.setFill("black")
arm2.draw(win)

mane = Polygon(Point(328,170),Point(311,207),Point(324,196),Point(326,217),Point(340,200),Point(350,211),Point(350,190),Point(364,195),Point(331,163))
mane.setFill("black")
mane.draw(win)

rei1 = Polygon(Point(371,140),Point(283,97),Point(282,102),Point(368,143))
rei1.setFill("green")
rei1.draw(win)

rei2 = Polygon(Point(405,179),Point(404,182),Point(293,143),Point(294,138))
rei2.setFill("green")
rei2.draw(win)

rei3 = Polygon(Point(285,102),Point(289,142),Point(295,143),Point(287,103))
rei3.setFill("green")
rei3.draw(win)

otherHair = Polygon(Point(386,135),Point(404,148),Point(395,149),Point(393,156),Point(386,152),Point(382,157),Point(377,153),Point(373,156),Point(384,136))
otherHair.setFill("black")
otherHair.draw(win)

copy = Text(Point(244,433),"(C) Can Stock Photo - csp8622003").draw(win)
#for i in range(100):
#     x = win.getMouse()
#     print("Point({},{}),".format(x.getX(),x.getY()),end="")
#     pn = Point(x.getX(),x.getY())
#     pn.draw(win)
          
    
