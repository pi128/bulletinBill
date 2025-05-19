from table3inserttemp import insert_sunday

insert_sunday(
    db_path="/Users/james/bulletinBill/IAC-Bulletin.db",
    name="Fifth Sunday in Lent",
    season="Lent",
    
    collect=(
        "We beseech thee, Almighty God, mercifully to look upon thy people; "
        "that by thy great goodness they may be governed and preserved evermore, both in body and soul; "
        "through Jesus Christ our Lord. Amen."
    ),
    first_lesson=(
        "I will make a new covenant with the house of Israel, and with the house of Judah:\n"
        "Not according to the covenant that I made with their fathers in the day that I took them by the hand "
        "to bring them out of the land of Egypt; which my covenant they brake, although I was an husband unto them, saith the Lord:\n"
        "But this shall be the covenant that I will make with the house of Israel; "
        "After those days, saith the Lord, I will put my law in their inward parts, and write it in their hearts; "
        "and will be their God, and they shall be my people."
    ),
    first_ref="Jeremiah 31:31–33",
    
    psalm=(
        "Many a time have they fought against me from my youth up: may Israel now say.\n"
        "Yea, many a time have they vexed me from my youth up: but they have not prevailed against me.\n"
        "The plowers plowed upon my back: and made long furrows.\n"
        "But the righteous Lord: hath hewn the snares of the ungodly in pieces."
    ),
    psalm_ref="Psalm 129:1–4",
    
    second_lesson=(
        "Christ being come an high priest of good things to come, by a greater and more perfect tabernacle, not made with hands, "
        "that is to say, not of this building;\n"
        "Neither by the blood of goats and calves, but by his own blood he entered in once into the holy place, "
        "having obtained eternal redemption for us.\n"
        "For if the blood of bulls and of goats, and the ashes of an heifer sprinkling the unclean, sanctifieth to the purifying of the flesh:\n"
        "How much more shall the blood of Christ, who through the eternal Spirit offered himself without spot to God, "
        "purge your conscience from dead works to serve the living God?"
    ),
    second_ref="Hebrews 9:11–14",
    
    gospel=(
        "Jesus said unto them, Verily, verily, I say unto you, Before Abraham was, I am.\n"
        "Then took they up stones to cast at him: but Jesus hid himself, and went out of the temple, "
        "going through the midst of them, and so passed by.\n"
        "And as Jesus passed by, he saw a man which was blind from his birth.\n"
        "And his disciples asked him, saying, Master, who did sin, this man, or his parents, that he was born blind?\n"
        "Jesus answered, Neither hath this man sinned, nor his parents: but that the works of God should be made manifest in him."
    ),
    gospel_ref="John 8:58–9:3",
    
    liturgical_order=21
)