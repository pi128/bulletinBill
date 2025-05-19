package liturgical

import "time"

type LiturgicalDay struct {
    Season string
    Number int
    Tags   []string
}

func GetLiturgicalDay(date time.Time) LiturgicalDay {
    // TODO: Replace with real season logic (like Easter calc)
    return LiturgicalDay{
        Season: "Easter",
        Number: 3,
        Tags:   []string{"Sunday"},
    }
}