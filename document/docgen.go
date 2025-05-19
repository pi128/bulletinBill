package document

import (
    "github.com/baliance/gooxml/document"
    "church-bulletin/liturgical"
)

func GenerateBulletinDocx(day liturgical.LiturgicalDay, filepath string) error {
    doc := document.New()

    doc.AddParagraph().AddRun().AddText("Incarnation Anglican Church Bulletin")
    doc.AddParagraph().AddRun().AddText("Season: " + day.Season)
    doc.AddParagraph().AddRun().AddText("Week: " + string(rune(day.Number)))

    for _, tag := range day.Tags {
        doc.AddParagraph().AddRun().AddText("Tag: " + tag)
    }

    return doc.SaveToFile(filepath)
}