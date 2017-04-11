#  -*- coding: utf8 -*-
# Exercise 35: Branches and Functions

# 234567890123456789012345678901234567890123456789012345678901234567890123456789

from sys import exit

phoenix = """
         __..--''``---....___   _..._    __
     _.-'    .-/";  `        ``<._  ``.''_ `.
 _.-' _..--.'_    \                    `( ) )
(_..-'    (< _     ;_..__               ; `'
           `-._,_)'      ``--...____..-'
"""
aslan = """
                      ,/\,,,,/\,.
                     =          =,
                    =` '<Q> <Q>'  =,
         ,=~~~~~~~~~`=     Y    =,`;,
       ,='            // :-^-; \\  `;
     ,='       `      ,,,,.'       :;
     ;,        '`          ':      `;
     ;`         ;',          ::,   ;;
     '\`   `,`';'`'`;`'`;';,  `; ':;
      '\`  '`\;~~~;/~~;~;/\`,  ';'`;
        \`  `'\             )),';~
        \`  '`\\             ))_;
        \`'`'\\
         \`'`\\
          `\\\`
"""

park = """
               ,@@@@@@@,
       ,,,.   ,@@@@@@/@@,  .oo8888o.
    ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o
   ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'
   %&&%&%&/%&&%@@\@@/ /@@@88888\88888'
   %&&%/ %&%%&&@@\ V /@@' `88\8 `/88'
   `&%\ ` /%&'    |.|        \ '|8'
       |o|        | |         | |
       |.|        | |         | |
jgs \\/ ._\//_/__/  ,\_//__\\/.  \_//__/_
"""


sunset = "SUNSET SUNSET SUNSET IMAGE"

aslan_and_anne = """
                      ,/\,,,,/\,.                ---====D                        @
                     =          =,      o                 ,,*:*::,.__     *             
                    =` '<Q> <Q>'  =,                   * ,)))*))))* __.=-.             o
         ,=~~~~~~~~~`=     Y    =,`;,        |       ,((*((a a))-'     
       ,='            // :-^-; \\  `;       -O-    ,))))))\ = /                     =( =     +
     ,='       `      ,,,,.'       :;  +     |    ,(((*(((()-(               *
     ;,        '`          ':      `;             *))))))/    `\    
     ;`         ;',          ::,   ;;             (((*}(//(_|_)\\                        .
     '\`   `,`';'`'`;`'`;';,  `; ':;              )*))))\\*).( //            +  .
      '\`  '`\;~~~;/~~;~;/\`,  ';'`;     *        (((((*(// / )/                   |
        \`  `'\             )),';~                 ))))))/ / /`                   -O-     @
        \`  '`\\             ))_;      +           `(*(((/ /`                      |
        \`'`'\\                                  o  `)))*))`\            *      
         \`'`\\                                       `((((  `-.__     ,      .  
          `\\\`                             .            *)-._    `--~jgs`
                                        @                +    `~---~~`                *
                                                     *       .            o         +
"""

piano = """
       _________________________
     |\ .-------|:::/:::|--------;
     |\|_  ___ _|:::/:::| __ ____|
     | ` __  ___\"\"\" \"\"\"_ ______  `\\
     | |\##\\###\\##\\###\\##\\### \\
     | \ \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ \\
     | | ;\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\";\"|
     | | |\"\"\"\"\"\".----------.\"\"\"\"\"\"| |
     | | |-----|\\___________\-|  | |
 jgs | | |     | |---------- |  \ | |
     `\| |     | |         | |   `| |
       \_|       |           |    `\|
"""

eis = """
         _____________
       /.-------------.\\\\
      //  \\\\            \\\\       
     //    \\\\-\"`\'\"-.     \\\\
    ||    / \\\\--\\'--`\    ||
    ||    |  \\\\      |    || 
    ||     \--\\\\--.-/     ||
    ||      \\=-\\\\=-/      ||
     \\\\      \\=-\\\\/      //
      \\\\      \\=-\\\\     //
       \\\\______\/_\\\\___//
         \'------------\'
"""

night = """      
.              .         .       |      *                      .   *        .       .
   *             *              -O-          .       *      -0-
         .             *         |     ,          .                .  *       - )-
o *                .           o       .      *       o       .          *
          .---.                                  o                |         o       .      *
    =   _/__~0_\_     .  *            o       '            .     -O-  .   *                .
 = = = (_________)             .              .                   |               . 
                 .                        *          *  o     .    '       *               
       *               - ) -       *                           *               - ) -       *        
"""


def start():
    ink = 0
    
    print
    print "----== Choices: A Prelude ==----"
    print "Meet Aslan, an orange cat large as a lion but less fierce, and Anne, as"
    print "mysterious as the moon, but far less distant."
    print
    print aslan_and_anne
    print
    print "Having had breakfast together at HOME, they are ready to go out for the day."
    print

    while True:
        choice = raw_input("\nShall we go to the PARK, or visit the TATTOO PARLOUR? ").lower()

        if "park" in choice:
            park(ink)
        elif "tattoo" in choice:
            print "Lucky the TATTOO PARLOUR is just over there.  Let's go!"
            tattoo()
        elif "home" in choice:
            end(0, 0, 0)
        else:
            print "But, surely - HOME, the PARK, or TATTOO PARLOUR?"


def park(is_there_a_tattoo):
    ink = int(is_there_a_tattoo)

    print "\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"
    print "----== The PARK! A great place to go, and now you're there!! ==----"
    print
    print "*** DEBUG *** ink has the value: %r" % ink
    print
    print "Oh, do look!  Under the trees, just beyond the Wasserspielplatz!"
    print "Phönix the white cat, as large as a lion but less fierce, is leading"
    print "a tai-chi class.  So graceful ...."

    park_choice(ink)


def park_choice(is_there_a_tattoo):
    ink = int(is_there_a_tattoo)
    
    print
    print "*** DEBUG *** ink has the value: %r" % ink
    print
    
    park_choice = raw_input("\nWould you like to TALK to Phönix, or WAIT for a bit? ").lower()

    if park_choice == 'talk' and ink == 1:
        print "\nPhönix finishes the last tai chi form with a grand sweep of her tail."
        print "She comes over and admires Aslan's claw tattoo by placing her paw on his"
        print "and rolling to her side at the same time.  It is a good sign."
        print phoenix
        end(1, 1, 0)
    elif park_choice == 'wait':
        park_life(ink)
    else:
        end(0, 1, art_choice)


def park_life(is_there_a_tattoo):
    ink = int(is_there_a_tattoo)
    a = "Through the trees, the sun dapples down."
    b = "So many leaves, tapping together to make a hissing noise like gentle rain."
    c = "A lovely breeze makes Aslan's hair move about." 
    
    park_life_descriptions = [a, b, c]
    
    print
    print "*** DEBUG *** ink has the value: %r" % ink
    print
    
    print "\tAnne and Aslan sit on the lush, clean grass."
    
    while True:
        for idyll in park_life_descriptions:
            print "\t%s" % idyll
            stay_or_go = raw_input("\t\nWould you like to stay in this IDYLL, or go and TALK to Phönix? ").lower()
            
            if "talk" in stay_or_go:
                end(ink, 1, 0)
            else:
                park_life(ink)
            
    park_choice(ink)
    
    
def tattoo():

    print "\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"
    print "----== The TATTOO PARLOUR ==----"
    print
    print "An extremely normal person approaches you.  They could be your accountant."
    print "They say, \'Hello, dear potential customer\'"
    print "They say, \'My, what lovely claws you have.\'"
    print "They say, \'Please look through our book of art.\'"
    print ".... and place a large book in front of you."
    print
    print "Press enter if you are ready to look at the tattoos."
    
    raw_input()
    tattoo_life()


def tattoo_life():    
    a = "A Leafy Sea Dragon floating through \n\tan ocean of stars and tiny cadillacs ..."
    a1 = "a leafy sea dragon."
    b = "Five tumbling laughing sumo wrestlers, \n\ttheir hair wantonly undone in a swirl of black lines ... "
    b1 = "five wanton wrestlers."
    c = "A single candle flame being blown out, \n\tthe last smoke a curlicue of cantor dust ..."
    c1 = "a cantor candle."
    d = "A climbing vine stemming from between two toes, \n\tand whose fruit and flowers hang over a shoulder ..."
    d1 = "an steady vine."
    
    art_book = [[a, a1], [b, b1], [c, c1], [d, d1]]
    art_choice = 0
    
    while art_choice == 0:
        for page, desc in art_book:
            print "\n\t%s" % page
            select_art = raw_input("\tCHOOSE this tattoo or look at MORE? ").lower()
            
            if 'choose' in select_art:
                print "\n\tThe accountant tattoos Aslan's claws with %s" % desc
                print "\tIt is truly beautiful."
                print
                art_choice = desc
                where_now = raw_input("\tDo you go HOME, or vist the PARK? ").lower()
                
                if "home" in where_now:
                    end(1, 0, art_choice)
                else:
                    park(1)
            else:
                art_choice = 0
                
    tattoo_life()
            

def end(ink, phoenix, art_choice):

    if ink == 0 and phoenix == 0:
        print "\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"
        print "----== HOME AGAIN ==----"
        print "Good idea.  This sunlight is not for the likes of us."
        print "Ahhh ... HOME's shady calm."
        print "In this world, There Is No Eis."
        print
        print "YOU WIN!"
        print
        print eis
        print
        print "°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"
        print "°°°°°°°°°°°°°°°°°° T H E °°°°°°°°°°° E N D °°°°°°°°°°°°°°°°°°°°°°°°°°°"
        print "°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"
        exit(0)
    elif ink == 0 and phoenix == 1:
        print "\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"
        print " ----== SUNSET ==----"
        print "Phönix says nothing, but points to the sky, where the sun is now setting."
        print "The children run away to hunt down wild Eis in the shrubbery."
        print "You put your hand in Aslan's ruff, and he and Phönix curl their tailtips around each other."
        print "Together, you prowl the parks of Berlin in the gathering dusk."
        print
        print "A majestic and elegant WIN!"
        print
        print sunset
        print
        print "°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"
        print "°°°°°°°°°°°°°°°°°° T H E °°°°°°°°°°° E N D °°°°°°°°°°°°°°°°°°°°°°°°°°°"
        print "°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"
        exit(0)
    elif ink == 1 and phoenix == 0:
        print "\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"
        print "----== SAG BESCHEID ==----"
        print "Such a great claw tattoo of %s. Meny must know of its pure awesome." % art_choice
        print "Anne helps Aslan to tweet it out to his followers."
        print
        print "YOU BOTH WIN!"
        print
        print "°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"
        print "°°°°°°°°°°°°°°°°°° T H E °°°°°°°°°°° E N D °°°°°°°°°°°°°°°°°°°°°°°°°°°"
        print "°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"
        exit(0)
    elif ink == 1 and phoenix == 1:
        print "\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"
        print "----== THE PIANO PARLOUR ==----"
        print "You all go home for an evening with friends."
        print "Anne plays songs, Aslan and Phönix sit atop the piano purring."
        print "A fine gathering, and all the glasses are put away before bedtime."
        print
        print "EVERYONE WINS!"
        print
        print piano
        print
        print 
        print "°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"
        print "°°°°°°°°°°°°°°°°°° T H E °°°°°°°°°°° E N D °°°°°°°°°°°°°°°°°°°°°°°°°°°"
        print "°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"
        exit(0)

print "°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"
print "----== The Piano in the Parlour ==----"
print "An afternoon adventure, with four possible endings."
print
raw_input("When you are ready, press any key ... ")
start()


print
print

print "======================================================================="