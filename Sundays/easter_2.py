from table3inserttemp import insert_sunday

insert_sunday(
    db_path="/Users/james/bulletinBill/IAC-Bulletin.db",
    name="First Sunday after Easter",
    season="Easter",
    
    collect=(
        "Almighty Father, who hast given thine only Son to die for our sins, and to rise again for our justification; "
        "Grant us so to put away the leaven of malice and wickedness, that we may always serve thee in pureness of living and truth; "
        "through the merits of the same thy Son Jesus Christ our Lord. Amen."
    ),
    first_lesson=(
        "And they continued stedfastly in the apostles’ doctrine and fellowship, and in breaking of bread, and in prayers.\n"
        "And fear came upon every soul: and many wonders and signs were done by the apostles.\n"
        "And all that believed were together, and had all things common;\n"
        "And sold their possessions and goods, and parted them to all men, as every man had need.\n"
        "And they, continuing daily with one accord in the temple, and breaking bread from house to house, "
        "did eat their meat with gladness and singleness of heart."
    ),
    first_ref="Acts 2:42–46",
    
    psalm=(
        "Behold, how good and joyful a thing it is: brethren to dwell together in unity.\n"
        "It is like the precious ointment upon the head, that ran down unto the beard: even unto Aaron’s beard, "
        "and went down to the skirts of his clothing.\n"
        "Like as the dew of Hermon: which fell upon the hill of Sion.\n"
        "For there the Lord promised his blessing: and life for evermore."
    ),
    psalm_ref="Psalm 133",
    
    second_lesson=(
        "Whatsoever is born of God overcometh the world: and this is the victory that overcometh the world, even our faith.\n"
        "Who is he that overcometh the world, but he that believeth that Jesus is the Son of God?\n"
        "This is he that came by water and blood, even Jesus Christ; not by water only, but by water and blood.\n"
        "And it is the Spirit that beareth witness, because the Spirit is truth."
    ),
    second_ref="1 John 5:4–6",
    
    gospel=(
        "Then the same day at evening, being the first day of the week, when the doors were shut where the disciples were assembled "
        "for fear of the Jews, came Jesus and stood in the midst, and saith unto them, Peace be unto you.\n"
        "And when he had so said, he shewed unto them his hands and his side. Then were the disciples glad, when they saw the Lord.\n"
        "Then said Jesus to them again, Peace be unto you: as my Father hath sent me, even so send I you.\n"
        "And when he had said this, he breathed on them, and saith unto them, Receive ye the Holy Ghost."
    ),
    gospel_ref="John 20:19–22",
    
    liturgical_order=24
)