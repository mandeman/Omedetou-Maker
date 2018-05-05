import moviepy.editor as mp

video = mp.VideoFileClip("Omedetou.mp4")

cong = "Trump.png"

shinji_smol = (mp.ImageClip(cong)
          .set_duration(12.9)
          .resize(height=35) # if you need to resize...
          .margin(left=477, top=145, opacity=0) # (optional) logo-border padding
          .set_pos(("left","top")))

shinji_big = (mp.ImageClip(cong)
          .set_start(12.9)
          .set_duration(1.5)
          .resize(height=550) # if you need to resize...
          .margin(left=305, top=0, opacity=0) # (optional) logo-border padding
          .set_pos(("left","top")))

misato_big = (mp.ImageClip("Cruz.png")
          .set_start(14.4)
          .set_duration(1.2)
          .resize(height=500) # if you need to resize...
          .margin(left=275, top=0, opacity=0) # (optional) logo-border padding
          .set_pos(("left","top")))

asuka_big = (mp.ImageClip("Jeb.png")
          .set_start(15.6)
          .set_duration(1.4)
          .resize(height=500) # if you need to resize...
          .margin(left=295, top=0, opacity=0) # (optional) logo-border padding
          .set_pos(("left","top")))

rei_big = (mp.ImageClip("Ben.png")
          .set_start(17)
          .set_duration(1.2)
          .resize(height=500) # if you need to resize...
          .margin(left=305, top=0, opacity=0) # (optional) logo-border padding
          .set_pos(("left","top")))

akagi_big = (mp.ImageClip("Rubio.png")
          .set_start(18.2)
          .set_duration(1.2)
          .resize(height=500) # if you need to resize...
          .margin(left=505, top=0, opacity=0) # (optional) logo-border padding
          .set_pos(("left","top")))

kaji_big = (mp.ImageClip("Gary.png")
          .set_start(19.4)
          .set_duration(1.15)
          .resize(height=515) # if you need to resize...
          .margin(left=95, top=35, opacity=0) # (optional) logo-border padding
          .set_pos(("left","top")))

hikari_big = (mp.ImageClip("Jill.png")
          .set_start(20.55)
          .set_duration(1.27)
          .resize(height=515) # if you need to resize...
          .margin(left=495, top=35, opacity=0) # (optional) logo-border padding
          .set_pos(("left","top")))

aida_big = (mp.ImageClip("Oliver.png")
          .set_start(20.55+1.27)
          .set_duration(23.03-20.55 - 1.27)
          .resize(height=500) # if you need to resize...
          .margin(left=125, top=15, opacity=0) # (optional) logo-border padding
          .set_pos(("left","top")))

touji_big = (mp.ImageClip("Stewart.png")
          .set_start(23.03)
          .set_duration(25.65-23.03)
          .resize(height=515) # if you need to resize...
          .margin(left=485, top=15, opacity=0) # (optional) logo-border padding
          .set_pos(("left","top")))

makoto_big = (mp.ImageClip("Pence.png")
          .set_start(25.65)
          .set_duration(1.2)
          .resize(height=515) # if you need to resize...
          .margin(right=515, top=15, opacity=0) # (optional) logo-border padding
          .set_pos(("right","top")))

aoba_big = (mp.ImageClip("Obama.png")
          .set_start(26.85)
          .set_duration(1.35)
          .resize(height=515) # if you need to resize...
          .margin(right=45, top=35, opacity=0) # (optional) logo-border padding
          .set_pos(("right","top")))

maya_big = (mp.ImageClip("Bush.png")
          .set_start(28.2)
          .set_duration(1.2)
          .resize(height=515) # if you need to resize...
          .margin(right=515, top=25, opacity=0) # (optional) logo-border padding
          .set_pos(("right","top")))

fuyutsuki_big = (mp.ImageClip("Bernie.png")
          .set_start(29.4)
          .set_duration(1.4)
          .resize(height=525) # if you need to resize...
          .margin(right=45, top=35, opacity=0) # (optional) logo-border padding
          .set_pos(("right","top")))

yui_big = (mp.ImageClip("Hillary.png")
          .set_start(30.8)
          .set_duration(1.73)
          .resize(height=300) # if you need to resize...
          .margin(right=165, top=110, opacity=0) # (optional) logo-border padding
          .set_pos(("right","top")))

gendo_big = (mp.ImageClip("Bill.png")
          .set_start(30.8)
          .set_duration(1.73)
          .resize(height=350) # if you need to resize...
          .margin(right=490, top=45, opacity=0) # (optional) logo-border padding
          .set_pos(("right","top")))

shinji_end = (mp.ImageClip(cong)
          .set_start(30.8+1.73)
          .set_duration(2.7)
          .resize(height=550)  # if you need to resize...
          .margin(right=245, top=0, opacity=0)  # (optional) logo-border padding
          .set_pos(("right","top")))

final = mp.CompositeVideoClip([video,
                               shinji_smol,
                               shinji_big,
                               misato_big,
                               asuka_big,
                               rei_big,
                               akagi_big,
                               kaji_big,
                               hikari_big,
                               aida_big,
                               touji_big,
                               makoto_big,
                               aoba_big,
                               maya_big,
                               fuyutsuki_big,
                               yui_big,
                               gendo_big,
                               shinji_end])

final.subclip(0, 35.2).write_videofile("test.mp4")
#final.subclip(20, 24).write_videofile("test.mp4")