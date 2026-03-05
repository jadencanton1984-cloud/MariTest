default score = 0

image questionbox = "images/Quiz/questionbox.png"

screen score_hud():

    frame:
        xalign 0.98
        yalign 0.02
        padding (15, 10)

        text "Score: [score]":
            size 28
            color "#ffffff"
            outlines [(2, "#000000", 0, 0)]

screen image_quiz():

    # Left Image (Correct Example)
    imagebutton:
        idle "jill1" at quiz_size
        xpos 630
        ypos 200
        action [SetVariable("score", score + 100), Jump("correct_answer")]

    # Right Image (Wrong Example)
    imagebutton:
        idle "jane1" at quiz_size
        xpos 1260
        ypos 200
        action Jump("wrong_answer")

label quiz_start:

    scene quiz city

    show screen score_hud

    show q normal at half_size

    q "Let's begin the assessment."

    jump question1

label question1:

    $ score = 0
    
    call screen image_quiz

label quiz_end:

    scene quiz city

    show q normal at half_size with dissolve

    q "Let's not repeat "

    jump explanation

label correct_answer:

    q "Correct!"
    
    q "Your score is now [score]!"
    
    jump explanation


label wrong_answer:

    q "Wrong!"
    
    jump explanation

label explanation:

    scene quiz city

    show q normal at half_size with dissolve

    q "You're wrong because I'm right."
    return

# authentic pics

image james1 = "images/dataset/AUTHENTIC/james1.png"
image james2 = "images/dataset/AUTHENTIC/james2.png"
image james3 = "images/dataset/AUTHENTIC/james3.png"
image james4 = "images/dataset/AUTHENTIC/james4.png"
image james5 = "images/dataset/AUTHENTIC/james5.png"
image james6 = "images/dataset/AUTHENTIC/james6.png"
image james7 = "images/dataset/AUTHENTIC/james7.png"
image james8 = "images/dataset/AUTHENTIC/james8.png"
image james9 = "images/dataset/AUTHENTIC/james9.png"
image james10 = "images/dataset/AUTHENTIC/james10.png"
image james11 = "images/dataset/AUTHENTIC/james11.png"
image james12 = "images/dataset/AUTHENTIC/james12.png"
image james13 = "images/dataset/AUTHENTIC/james13.png"
image james14 = "images/dataset/AUTHENTIC/james14.png"
image james15 = "images/dataset/AUTHENTIC/james15.png"
image james16 = "images/dataset/AUTHENTIC/james16.png"
image james17 = "images/dataset/AUTHENTIC/james17.png"
image james18 = "images/dataset/AUTHENTIC/james18.png"
image james19 = "images/dataset/AUTHENTIC/james19.png"
image james20 = "images/dataset/AUTHENTIC/james20.png"

image jane1 = "images/dataset/AUTHENTIC/jane1.png"
image jane2 = "images/dataset/AUTHENTIC/jane2.png"
image jane3 = "images/dataset/AUTHENTIC/jane3.png"
image jane4 = "images/dataset/AUTHENTIC/jane4.png"
image jane5 = "images/dataset/AUTHENTIC/jane5.png"
image jane6 = "images/dataset/AUTHENTIC/jane6.png"
image jane7 = "images/dataset/AUTHENTIC/jane7.png"
image jane8 = "images/dataset/AUTHENTIC/jane8.png"
image jane9 = "images/dataset/AUTHENTIC/jane9.png"
image jane10 = "images/dataset/AUTHENTIC/jane10.png"
image jane11 = "images/dataset/AUTHENTIC/jane11.png"
image jane12 = "images/dataset/AUTHENTIC/jane12.png"
image jane13 = "images/dataset/AUTHENTIC/jane13.png"
image jane14 = "images/dataset/AUTHENTIC/jane14.png"
image jane15 = "images/dataset/AUTHENTIC/jane15.png"
image jane16 = "images/dataset/AUTHENTIC/jane16.png"
image jane17 = "images/dataset/AUTHENTIC/jane17.png"
image jane18 = "images/dataset/AUTHENTIC/jane18.png"
image jane19 = "images/dataset/AUTHENTIC/jane19.png"
image jane20 = "images/dataset/AUTHENTIC/jane20.png"

# deepfake pics

image john1 = "images/dataset/DEEPFAKES PLAIN/john1.png"
image john2 = "images/dataset/DEEPFAKES PLAIN/john2.png"
image john3 = "images/dataset/DEEPFAKES PLAIN/john3.png"
image john4 = "images/dataset/DEEPFAKES PLAIN/john4.png"
image john5 = "images/dataset/DEEPFAKES PLAIN/john5.png"
image john6 = "images/dataset/DEEPFAKES PLAIN/john6.png"
image john7 = "images/dataset/DEEPFAKES PLAIN/john7.png"
image john8 = "images/dataset/DEEPFAKES PLAIN/john8.png"
image john9 = "images/dataset/DEEPFAKES PLAIN/john9.png"
image john10 = "images/dataset/DEEPFAKES PLAIN/john10.png"
image john11 = "images/dataset/DEEPFAKES PLAIN/john11.png"
image john12 = "images/dataset/DEEPFAKES PLAIN/john12.png"
image john13 = "images/dataset/DEEPFAKES PLAIN/john13.png"
image john14 = "images/dataset/DEEPFAKES PLAIN/john14.png"
image john15 = "images/dataset/DEEPFAKES PLAIN/john15.png"
image john16 = "images/dataset/DEEPFAKES PLAIN/john16.png"
image john17 = "images/dataset/DEEPFAKES PLAIN/john17.png"
image john18 = "images/dataset/DEEPFAKES PLAIN/john18.png"
image john19 = "images/dataset/DEEPFAKES PLAIN/john19.png"
image john20 = "images/dataset/DEEPFAKES PLAIN/john20.png"

image jill1 = "images/dataset/DEEPFAKES PLAIN/jill1.png"
image jill2 = "images/dataset/DEEPFAKES PLAIN/jill2.png"
image jill3 = "images/dataset/DEEPFAKES PLAIN/jill3.png"
image jill4 = "images/dataset/DEEPFAKES PLAIN/jill4.png"
image jill5 = "images/dataset/DEEPFAKES PLAIN/jill5.png"
image jill6 = "images/dataset/DEEPFAKES PLAIN/jill6.png"
image jill7 = "images/dataset/DEEPFAKES PLAIN/jill7.png"
image jill8 = "images/dataset/DEEPFAKES PLAIN/jill8.png"
image jill9 = "images/dataset/DEEPFAKES PLAIN/jill9.png"
image jill10 = "images/dataset/DEEPFAKES PLAIN/jill10.png"
image jill11 = "images/dataset/DEEPFAKES PLAIN/jill11.png"
image jill12 = "images/dataset/DEEPFAKES PLAIN/jill12.png"
image jill13 = "images/dataset/DEEPFAKES PLAIN/jill13.png"
image jill14 = "images/dataset/DEEPFAKES PLAIN/jill14.png"
image jill15 = "images/dataset/DEEPFAKES PLAIN/jill15.png"
image jill16 = "images/dataset/DEEPFAKES PLAIN/jill16.png"
image jill17 = "images/dataset/DEEPFAKES PLAIN/jill17.png"
image jill18 = "images/dataset/DEEPFAKES PLAIN/jill18.png"
image jill19 = "images/dataset/DEEPFAKES PLAIN/jill19.png"
image jill20 = "images/dataset/DEEPFAKES PLAIN/jill20.png"

# explanation pics

image answerjohn1 = "images/dataset/DEEPFAKE ANSWER KEY/answermale1.png"
image answerjohn2 = "images/dataset/DEEPFAKE ANSWER KEY/answermale2.png"
image answerjohn3 = "images/dataset/DEEPFAKE ANSWER KEY/answermale3.png"
image answerjohn4 = "images/dataset/DEEPFAKE ANSWER KEY/answermale4.png"
image answerjohn5 = "images/dataset/DEEPFAKE ANSWER KEY/answermale5.png"
image answerjohn6 = "images/dataset/DEEPFAKE ANSWER KEY/answermale6.png"
image answerjohn7 = "images/dataset/DEEPFAKE ANSWER KEY/answermale7.png"
image answerjohn8 = "images/dataset/DEEPFAKE ANSWER KEY/answermale8.png"
image answerjohn9 = "images/dataset/DEEPFAKE ANSWER KEY/answermale9.png"
image answerjohn10 = "images/dataset/DEEPFAKE ANSWER KEY/answermale10.png"
image answerjohn11 = "images/dataset/DEEPFAKE ANSWER KEY/answermale11.png"
image answerjohn12 = "images/dataset/DEEPFAKE ANSWER KEY/answermale12.png"
image answerjohn13 = "images/dataset/DEEPFAKE ANSWER KEY/answermale13.png"
image answerjohn14 = "images/dataset/DEEPFAKE ANSWER KEY/answermale14.png"
image answerjohn15 = "images/dataset/DEEPFAKE ANSWER KEY/answermale15.png"
image answerjohn16 = "images/dataset/DEEPFAKE ANSWER KEY/answermale16.png"
image answerjohn17 = "images/dataset/DEEPFAKE ANSWER KEY/answermale17.png"
image answerjohn18 = "images/dataset/DEEPFAKE ANSWER KEY/answermale18.png"
image answerjohn19 = "images/dataset/DEEPFAKE ANSWER KEY/answermale19.png"
image answerjohn20 = "images/dataset/DEEPFAKE ANSWER KEY/answermale20.png"

image answerjill1 = "images/dataset/DEEPFAKE ANSWER KEY/answerfemale1.png"
image answerjill2 = "images/dataset/DEEPFAKE ANSWER KEY/answerfemale2.png"
image answerjill3 = "images/dataset/DEEPFAKE ANSWER KEY/answerfemale3.png"
image answerjill4 = "images/dataset/DEEPFAKE ANSWER KEY/answerfemale4.png"
image answerjill5 = "images/dataset/DEEPFAKE ANSWER KEY/answerfemale5.png"
image answerjill6 = "images/dataset/DEEPFAKE ANSWER KEY/answerfemale6.png"
image answerjill7 = "images/dataset/DEEPFAKE ANSWER KEY/answerfemale7.png"
image answerjill8 = "images/dataset/DEEPFAKE ANSWER KEY/answerfemale8.png"
image answerjill9 = "images/dataset/DEEPFAKE ANSWER KEY/answerfemale9.png"
image answerjill10 = "images/dataset/DEEPFAKE ANSWER KEY/answerfemale10.png"
image answerjill11 = "images/dataset/DEEPFAKE ANSWER KEY/answerfemale11.png"
image answerjill12 = "images/dataset/DEEPFAKE ANSWER KEY/answerfemale12.png"
image answerjill13 = "images/dataset/DEEPFAKE ANSWER KEY/answerfemale13.png"
image answerjill14 = "images/dataset/DEEPFAKE ANSWER KEY/answerfemale14.png"
image answerjill15 = "images/dataset/DEEPFAKE ANSWER KEY/answerfemale15.png"
image answerjill16 = "images/dataset/DEEPFAKE ANSWER KEY/answerfemale16.png"
image answerjill17 = "images/dataset/DEEPFAKE ANSWER KEY/answerfemale17.png"
image answerjill18 = "images/dataset/DEEPFAKE ANSWER KEY/answerfemale18.png"
image answerjill19 = "images/dataset/DEEPFAKE ANSWER KEY/answerfemale19.png"
image answerjill20 = "images/dataset/DEEPFAKE ANSWER KEY/answerfemale20.png"
