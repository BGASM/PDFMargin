# PDFMargin
### pyQT app to let you add wide-ass margins to PDFs for annotation

This app uses PyPDF2 to read an existing PDF and output a copy of it with enlarged margins.
GUI was written in pyQT5, using pysides2.

PDFMargin was made to help me quickly convert school PDFs so that I could take notes on them.
It works for me, I thought it would be nice to share. Understand that this app was made in a day and will most likely never be updated. There are surely bugs.
**Annotations will not carry over unless you flatten them to your PDF first. This means comments will be lost, but highlights and ink can be flattened and saved.**
**Bookmarks also will not carry over.** That sucks, I know. I couldn't figure it out and I didn't want to spend more time on it when I should be studying.

Use:
- Margins are in inches, and on BOTH sides. 10" does not mean 10" across, it means your document's original size, plus 10" on either side.
- You can enter decimals.
- Don't use negatives. I just realized I did not safeguard against it and it will probably make PyPDF2 throw an error. Or it might make it do something incredible...
- Enter input and output directory paths manually or use the explorer by clicking browse.
- If you enter paths manually make sure it is to a directory. There are checks to prevent you accidentally pathing to a file in the browse, but no such validation was included for manual.
- If you want to select individual files to add margins to click the corresponding check box. The browser will only show you pdfs within a directory if you run it in default mode.

Notes:
- Margins are capped at 10" because that alread seemed wild. If you need them to be larger, you can mod the source on Github
- App will do its best to validate file paths and catch errors and stop you from doing anything stupid. Always back up your data, especially if these PDFs are important.
- App will also check read and write permissions before attempting to create PDFs, which should prevent crashes.


