from PIL import Image, ImageDraw, ImageFilter
import math


photo_path = "static/images/Picture1 (2).jpg"


photo = Image.open(photo_path).convert("RGB")


# Canvas size
canvas = Image.new("RGB", (900,900), (0,0,0))


# Heart border

for t in range(0,360,8):

    angle = math.radians(t)


    # Heart formula

    x = 16 * math.sin(angle)**3

    y = -(13*math.cos(angle)
          -5*math.cos(2*angle)
          -2*math.cos(3*angle)
          -math.cos(4*angle))


    # Heart size

    x = int(x*32 + 450)

    y = int(y*32 + 450)



    # Small border photo

    small = photo.resize((55,55))


    mask = Image.new("L",(55,55),0)

    draw = ImageDraw.Draw(mask)


    draw.rounded_rectangle(
        (0,0,55,55),
        radius=12,
        fill=255
    )


    canvas.paste(
        small,
        (x-27,y-27),
        mask
    )



# Big center photo

big = photo.resize((280,350))


mask = Image.new("L",(280,350),0)

draw = ImageDraw.Draw(mask)


draw.rounded_rectangle(
    (0,0,280,350),
    radius=30,
    fill=255
)


canvas.paste(
    big,
    (310,280),
    mask
)



# Golden glow

glow = Image.new(
    "RGBA",
    canvas.size,
    (0,0,0,0)
)


draw = ImageDraw.Draw(glow)


draw.ellipse(
    (250,220,650,700),
    fill=(255,210,100,60)
)


glow = glow.filter(
    ImageFilter.GaussianBlur(60)
)



final = Image.alpha_composite(
    canvas.convert("RGBA"),
    glow
)



# Save

final.convert("RGB").save(
    "static/images/heart_photo.jpg"
)


print("❤️ Heart photo created!")