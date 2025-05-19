package main

import (
    "fmt"
    "os"
    "time"
    "os/exec"
    "church-bulletin/liturgical"
    "church-bulletin/document"
)

func main() {
    date := time.Now()
    if len(os.Args) > 1 {
        parsed, err := time.Parse("2006-01-02", os.Args[1])
        if err != nil {
            fmt.Println("Invalid date format. Use YYYY-MM-DD.")
            return
        }
        date = parsed
    }

    day := liturgical.GetLiturgicalDay(date)

    filename := fmt.Sprintf("output/bulletin_%s.docx", date.Format("2006-01-02"))
    err := document.GenerateBulletinDocx(day, filename)
    if err != nil {
        fmt.Println("Failed to generate bulletin:", err)
        return
    }

    fmt.Println("Bulletin saved:", filename)

    // Bonus: open in Pages
    exec.Command("open", "-a", "Pages", filename).Run()
}