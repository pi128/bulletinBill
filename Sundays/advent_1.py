from table3inserttemp import insert_sunday
import sqlite3
# Call the function to insert the First Sunday in Advent
insert_sunday(
    db_path="/Users/james/bulletinBill/IAC-Bulletin.db",
    name="First Sunday in Advent",
    season="Advent",
    collect=(
        "Almighty God, give us grace that we may cast away the works of darkness, "
        "and put upon us the armour of light, now in the time of this mortal life "
        "in which thy Son Jesus Christ came to visit us in great humility; that in the last day, "
        "when he shall come again in his glorious majesty to judge both the quick and the dead, "
        "we may rise to the life immortal; through him who liveth and reigneth with thee and the Holy Ghost, "
        "now and ever. Amen."
    ),
    first_lesson=(
        "The word that Isaiah the son of Amoz saw concerning Judah and Jerusalem.\n"
        "And it shall come to pass in the last days, that the mountain of the Lord’s house shall be established "
        "in the top of the mountains, and shall be exalted above the hills; and all nations shall flow unto it.\n"
        "And many people shall go and say, Come ye, and let us go up to the mountain of the Lord, to the house of the God of Jacob; "
        "and he will teach us of his ways, and we will walk in his paths: for out of Zion shall go forth the law, and the word of the Lord from Jerusalem.\n"
        "And he shall judge among the nations, and shall rebuke many people: and they shall beat their swords into plowshares, "
        "and their spears into pruninghooks: nation shall not lift up sword against nation, neither shall they learn war any more.\n"
        "O house of Jacob, come ye, and let us walk in the light of the Lord."
    ),
    first_ref="Isaiah 2:1–5",
    psalm=(
        "I was glad when they said unto me, Let us go into the house of the Lord.\n"
        "Our feet shall stand within thy gates, O Jerusalem.\n"
        "Jerusalem is builded as a city that is compact together:\n"
        "Whither the tribes go up, the tribes of the Lord, unto the testimony of Israel, "
        "to give thanks unto the name of the Lord.\n"
        "For there are set thrones of judgment, the thrones of the house of David.\n"
        "Pray for the peace of Jerusalem: they shall prosper that love thee.\n"
        "Peace be within thy walls, and prosperity within thy palaces.\n"
        "For my brethren and companions’ sakes, I will now say, Peace be within thee.\n"
        "Because of the house of the Lord our God I will seek thy good."
    ),
    psalm_ref="Psalm 122",
    second_lesson=(
        "And that, knowing the time, that now it is high time to awake out of sleep: "
        "for now is our salvation nearer than when we believed.\n"
        "The night is far spent, the day is at hand: let us therefore cast off the works of darkness, "
        "and let us put on the armour of light.\n"
        "Let us walk honestly, as in the day; not in rioting and drunkenness, not in chambering and wantonness, "
        "not in strife and envying.\n"
        "But put ye on the Lord Jesus Christ, and make not provision for the flesh, to fulfil the lusts thereof."
    ),
    second_ref="Romans 13:11–14",
    gospel=(
        "And when they drew nigh unto Jerusalem, and were come to Bethphage, unto the mount of Olives, "
        "then sent Jesus two disciples,\n"
        "Saying unto them, Go into the village over against you, and straightway ye shall find an ass tied, and a colt with her: "
        "loose them, and bring them unto me.\n"
        "And if any man say ought unto you, ye shall say, The Lord hath need of them; and straightway he will send them.\n"
        "All this was done, that it might be fulfilled which was spoken by the prophet, saying,\n"
        "Tell ye the daughter of Sion, Behold, thy King cometh unto thee, meek, and sitting upon an ass, "
        "and a colt the foal of an ass.\n"
        "And the disciples went, and did as Jesus commanded them,\n"
        "And brought the ass, and the colt, and put on them their clothes, and they set him thereon.\n"
        "And a very great multitude spread their garments in the way; others cut down branches from the trees, and strawed them in the way.\n"
        "And the multitudes that went before, and that followed, cried, saying, Hosanna to the Son of David: "
        "Blessed is he that cometh in the name of the Lord; Hosanna in the highest."
    ),
    gospel_ref="Matthew 21:1–9",
    liturgical_order=1
)