from table3inserttemp import insert_sunday

insert_sunday(
    db_path="/Users/james/bulletinBill/IAC-Bulletin.db",
    name="Fourth Sunday in Lent",
    season="Lent",
    
    collect=(
        "Grant, we beseech thee, Almighty God, that we, who for our evil deeds do worthily deserve to be punished, "
        "by the comfort of thy grace may mercifully be relieved; through our Lord and Saviour Jesus Christ. Amen."
    ),
    first_lesson=(
        "Rejoice ye with Jerusalem, and be glad with her, all ye that love her: rejoice for joy with her, all ye that mourn for her:\n"
        "That ye may suck, and be satisfied with the breasts of her consolations; "
        "that ye may milk out, and be delighted with the abundance of her glory.\n"
        "For thus saith the Lord, Behold, I will extend peace to her like a river, "
        "and the glory of the Gentiles like a flowing stream: "
        "then shall ye suck, ye shall be borne upon her sides, and be dandled upon her knees.\n"
        "As one whom his mother comforteth, so will I comfort you; and ye shall be comforted in Jerusalem."
    ),
    first_ref="Isaiah 66:10–13",
    
    psalm=(
        "They that sow in tears: shall reap in joy.\n"
        "He that now goeth on his way weeping, and beareth forth good seed:\n"
        "shall doubtless come again with joy, and bring his sheaves with him."
    ),
    psalm_ref="Psalm 126:6–8 (paraphrased)",
    
    second_lesson=(
        "Tell me, ye that desire to be under the law, do ye not hear the law?\n"
        "For it is written, that Abraham had two sons, the one by a bondmaid, the other by a freewoman.\n"
        "But he who was of the bondwoman was born after the flesh; but he of the freewoman was by promise.\n"
        "Which things are an allegory: for these are the two covenants."
    ),
    second_ref="Galatians 4:21–24",
    
    gospel=(
        "And Jesus went up into a mountain, and there he sat with his disciples.\n"
        "And the passover, a feast of the Jews, was nigh.\n"
        "When Jesus then lifted up his eyes, and saw a great company come unto him, he saith unto Philip, "
        "Whence shall we buy bread, that these may eat?\n"
        "And this he said to prove him: for he himself knew what he would do.\n"
        "Philip answered him, Two hundred pennyworth of bread is not sufficient for them, "
        "that every one of them may take a little.\n"
        "One of his disciples, Andrew, Simon Peter’s brother, saith unto him,\n"
        "There is a lad here, which hath five barley loaves, and two small fishes: but what are they among so many?\n"
        "And Jesus said, Make the men sit down."
    ),
    gospel_ref="John 6:3–10",
    
    liturgical_order=20
)