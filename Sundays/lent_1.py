from table3inserttemp import insert_sunday

insert_sunday(
    db_path="/Users/james/bulletinBill/IAC-Bulletin.db",
    name="First Sunday in Lent",
    season="Lent",
    
    collect=(
        "O Lord, who for our sake didst fast forty days and forty nights; "
        "Give us grace to use such abstinence, that, our flesh being subdued to the Spirit, "
        "we may ever obey thy godly motions in righteousness, and true holiness, "
        "to thy honour and glory, who livest and reignest with the Father and the Holy Ghost, one God, world without end. Amen."
    ),
    first_lesson=(
        "Is not this the fast that I have chosen? to loose the bands of wickedness, to undo the heavy burdens, "
        "and to let the oppressed go free, and that ye break every yoke?\n"
        "Is it not to deal thy bread to the hungry, and that thou bring the poor that are cast out to thy house? "
        "when thou seest the naked, that thou cover him; and that thou hide not thyself from thine own flesh?\n"
        "Then shall thy light break forth as the morning, and thine health shall spring forth speedily: "
        "and thy righteousness shall go before thee; the glory of the Lord shall be thy rearward."
    ),
    first_ref="Isaiah 58:6–8",
    
    psalm=(
        "He shall call upon me, and I will hear him: yea, I am with him in trouble;\n"
        "I will deliver him, and bring him to honour.\n"
        "With long life will I satisfy him: and show him my salvation."
    ),
    psalm_ref="Psalm 91:15–16",
    
    second_lesson=(
        "We then, as workers together with him, beseech you also that ye receive not the grace of God in vain.\n"
        "(For he saith, I have heard thee in a time accepted, and in the day of salvation have I succoured thee: "
        "behold, now is the accepted time; behold, now is the day of salvation.)\n"
        "Giving no offence in any thing, that the ministry be not blamed:\n"
        "But in all things approving ourselves as the ministers of God, in much patience, in afflictions, "
        "in necessities, in distresses."
    ),
    second_ref="2 Corinthians 6:1–4",
    
    gospel=(
        "Then was Jesus led up of the Spirit into the wilderness to be tempted of the devil.\n"
        "And when he had fasted forty days and forty nights, he was afterward an hungred.\n"
        "And when the tempter came to him, he said, If thou be the Son of God, command that these stones be made bread.\n"
        "But he answered and said, It is written, Man shall not live by bread alone, but by every word that proceedeth out of the mouth of God."
    ),
    gospel_ref="Matthew 4:1–4",
    
    liturgical_order=17
)