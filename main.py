#import modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from random import choice

#main app objects and settings
app = QApplication([])
main_window = QWidget()
#set window title and size (width, height)
main_window.setWindowTitle('Random Word Maker')
main_window.resize(300, 200)

#create all app ojects
title_text = QLabel('Random Word Maker')
#initial texts
text1 = QLabel('?')
text2 = QLabel('?')
text3 = QLabel('?')

#initial buttons
button1 = QPushButton('Click me')
button2 = QPushButton('Click me')
button3 = QPushButton('Click me')

#Random word list
word_list = ["lantern", "whisper", "avalanche", "mosaic", "orbit", "velvet", "crumble", "zephyr", "anchor", "ember", "spiral", "tundra", "parchment", "glimmer", "horizon", "mirage", "cobblestone", "echo", "bramble", "solstice", "cascade", "quartz", "meadow", "frost", "ember", "ripple", "grove", "voyage", "drift", "silhouette", "harbor", "crescent", "ember", "twilight", "breeze", "summit", "dawn", "meander", "crystal", "willow", "shadow", "harvest", "brook", "mist", "flint", "hollow", "sage", "serpent", "relic", "aurora", "spire", "petal", "gale", "ember", "meadowlark", "glade", "ash", "cinder", "blossom", "whistle", "brookstone", "thistle", "murmur", "flame", "haven", "tempest", "drizzle", "horizon", "meadowlight", "canyon", "wharf", "boulder", "root", "fern", "emberwood", "snowfall", "oasis", "groveland", "harvestmoon", "stillwater", "dust", "meadowrun", "quiver", "fog", "pine", "cliff", "echoes", "cobble", "stream", "flintlock", "moss", "glow", "breezehill", "hollowbrook", "raven", "trail", "willowbend", "solace"]



# All design here
master_layout = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

# Add widgets to layouts here
row1.addWidget(title_text, alignment=Qt.AlignCenter)

row2.addWidget(text1 , alignment=Qt.AlignCenter)
row2.addWidget(text2 , alignment=Qt.AlignCenter)
row2.addWidget(text3 , alignment=Qt.AlignCenter)

# Add buttons to layouts here
row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)

# Add rows to master layout here
master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

# Set main window layout
main_window.setLayout(master_layout)

# All functions here
def button1_clicked():
    word = choice(word_list)
    text1.setText(word)
def button2_clicked():
    word = choice(word_list)
    text2.setText(word)
def button3_clicked():
    word = choice(word_list)
    text3.setText(word)

# Events here
button1.clicked.connect(button1_clicked)
button2.clicked.connect(button2_clicked)
button3.clicked.connect(button3_clicked)


#show/run app
main_window.show()
app.exec_()


#Future improvements:
#1. Add more words to the word_list for greater variety.
#2. Implement a feature to combine the three words into a single phrase or sentence.
#3. Add styling to the app for a more appealing user interface.
#4. Include an option to save the generated words to a file.
#5. Add sound effects or animations when buttons are clicked.
#6. Allow users to input their own words to be included in the random selection.
#7. Implement a feature to generate words based on specific themes or categories.
#8. Add a reset button to clear the displayed words.
#9. Make the app responsive to different screen sizes and orientations.
#10. Include a history feature to view previously generated words.
#11. Add localization support for multiple languages.
#12. Implement a feature to share the generated words on social media platforms.
#13. Add keyboard shortcuts for button clicks.
#14. Include a timer to automatically generate new words at set intervals.
#15. Create a mobile version of the app for smartphones and tablets.
#16. Add a feature to customize the font style and size of the displayed words.
#17. Implement a dark mode for the app interface.
#18. Include a feature to pronounce the generated words using text-to-speech.
#19. Add a feature to filter words based on length or starting letter.
#20. Create a leaderboard to track the most frequently generated words.
#21. Implement a feature to categorize words into nouns, verbs, adjectives, etc.
#22. Add a feature to generate random sentences using the selected words.
#23. Include a feature to display the definition of the generated words.
#24. Add a feature to generate rhyming words based on the selected words.
#25. Validate the word list to ensure all entries are appropriate and non-repetitive.