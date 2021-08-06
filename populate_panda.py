import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'panda_ebooks.settings')

import django
django.setup()
from panda.models import Category, Book

def populate():
    Fiction_books = [
        {'name': 'Everything I Never Told You',
        'description': 'Lydia is the favourite child of Marilyn and James Lee; a girl who inherited her mothers bright blue eyes and her fathers jet-black','views':100,'likes':100},
        {'name': 'Because of Winn-Dixie?','description': 'classic tale by Newbery Medalist Kate DiCamillo, Americas beloved storyteller. One summer s day, ten-year-old India Opal Buloni goes down to the local supermarket for some groceries and comes home with a dog. But Winn-Dixie is no ordinary dog. It s because of Winn-Dixie that Opal begins to make friends. And it s because of Winn-Dixie that she finally dares to ask her father about her mother, who left when Opal was three. In fact, as Opal admits, just about everything that happens that summer is because of Winn-Dixie. Featuring a new cover illustration by E. B. Lewis.','views':100,'likes':100},
        {'name': 'A Thousand Splendid Suns','description': 'The first and most autobiographical ofMaugham\'smasterpieces.It is the story of Philip Carey, an orphaneager forlife, love an','views':70,'likes':40}]
    BiographiesAndMemories_books = [
        {'name': 'The Diary of a Young Girl','description': 'Discovered in the attic in which she spent the last years of herlife, Anne Frank\'s remarkable diary has since become a worldclassic--a powerful reminder of the horrors of war and an eloquenttestament to the human spirit. In 1942, with Nazis occupyingHolland, a thirteen-year-old Jewish girl and her family fled theirhome in Amsterdam and went into hiding. For the next two years,until their whereabouts were betrayed to the Gestapo, they andanother family lived cloistered in the "Secret Annex" of an oldoffice building. Cut off from the outside world, they faced hunger,boredom, the constant cruelties of living in confined quarter','views':100,'likes':100},
        {'name': 'Maus: A Survivor’s Tale','description': 'Acclaimed as a quiet triumph and a brutally moving work of art, the first volume of Art Spiegelmans Maus introduced readers to Vladek Spiegelman, a Jewish survivor of Hitlers Europe, and his son, a cartoonist trying to come to terms with his father, his fathers terrifying story, and History itself. Its form, the cartoon (the Nazis are cats, the Jews mice), succeeds perfectly in shocking us out of any lingering sense of familiarity with the events described, approaching, as it does, the unspeakable through the diminutive. This second volume, subtitled And Here My Troubles Began, mov','views':80,'likes':100},
        {'name': 'I Know Why the Caged Bird Sings', 'description': 'Sent by their mother to live with their devout,self-sufficientgrandmother in a small Southern town, Maya and herbrother,Bailey,endure the ache of abandonment and the prejudice ofthelocal "powhitetrash." At eight years old and back at hermother\'sside in St. Louis, Maya is attacked by a man many times herage-andhas to live with the consequences for a lifetime. Yearslater, inSan Francisco, Maya learns about love for herself and thekindnessof others, her own strong spirit, and the ideas of greatauthors("I met and fell in love with William Shakespeare") willallow herto be free instead of imprisoned. Poetic and powerful, I Know W','views':100,'likes':70}]
    Literature_books = [
        {'name': 'Twenty Love Poems and a Song of D','description': 'When it appeared in 1924, this work launched into the international spotlight a young, unknown poet whose writings would ignite a generation. Merwin’s incomparable translation faces the original Spanish text in this volume that continues to inspire lovers and poets','views':70,'likes':80},
        {'name': 'A Raisin in the Sun', 'description': 'When it was first produced in 1959, A Raisin in the Sun was awarded the New York Drama Critics Circle Award for that season and hailed as a watershed in American drama. A pioneering work by an African-American playwright, the play was a radically new representation of black life. " A play that changed American theater forever." --The New York Times','views':80,'likes':90},
        {'name': 'Inherit the Wind', 'description': 'A classic work of American theatre, based on the Scopes Monkey Trial of 1925, which pitted Clarence Darrow against William Jennings Bryan in defense of a schoolteacher accused of teaching the theory of evolution The accused was a slight, frightened man who had deliberately broken the law. His trial was a Roman circus.','views':100,'likes':120}]
    HumanitiesAndSocialScience_books = [
        {'name': 'Men are from Mars, Women are from Venus','description': 'he most well-know,long-lived,andtried-and-testedrelationships guide ever,thephenomenal#1 NewYorkTimes bestseller Men Are From Mars, WomenAreFromVenus isnow available for the first timeeverintrade paperback. In thisclassic guide tounderstanding the opposite sex','views':100,'likes':1060},
        {'name': 'Man’s Search for Meaning','description': 'Psychiatrist Viktor Frankl s memoir has riveted generations of readers with its de*ions of life in Nazi death camps and its lessons for spiritual survival. Between 1942 and 1945 Frankl labored in four different camps, including Auschwitz, while his parents, brother, and pregnant wife perished.','views':100,'likes':170},
        {'name': 'The Design of Everyday Things', 'description': 'ven the smartest among us can feel inept as we fail tofigureoutwhich light switch or oven burner to turn on, or whethertopush,pull, or slide a door. The fault, arguesthisingenious--evenliberating--book, lies not in ourselves, butinproduct design thatignores the needs of users and the principlesofcognitivepsychology.','views':170,'likes':180}]
    TravelGuid_books = [
        {'name': 'A Walk in the Woods: Rediscovering America on the Appala','description': 'he Appalachian Trail trail stretches from Georgia to Maineandcovers some of the most breathtaking terrain inAmerica majesticmountains, silent forests, sparking lakes.','views':100,'likes':100},
        {'name': 'The Art of Travel','description': 'Any Baedeker will tell us "where" we ought to travel, but only Alain de Botton will tell us "how" and "why. "With the same intelligence and insouciant charm he brought to How Proust Can Save Your Life," "de Botton considers the pleasures of anticipation','views':100,'likes':100},
        {'name': 'Underthe Tuscan Sun, At Home In Italy', 'description': 'Twenty years ago, Frances Mayes','views':100,'likes':100}]
    ComputerAndInternet_books = [
        {'name': 'The Little Schemer The MIT P','description': 'The notion that "thinking about computing is one of the most exciting things the human mind can do" sets both The Little Schemer (formerly known as The Little LISPer) and its new companion volume, The Seasoned Schemer, apart from other books on LISP.','views':100,'likes':100},
        {'name': 'Linux Device Drivers','description': 'Device drivers literally drive everything you are interested in--disks, monitors, keyboards, modems everything outside the computer chip and memory.','views':100,'likes':100},
        {'name': 'McSa/MCSE Self-Paced Training Kit (Exam 70-216)','description': 'The two LNAI volumes 7208 and 7209 constitute the proceedings of the 7th International Conference on Hybrid Artificial Intelligent Systems, HAIS 2012, held in Salamanca, Spain, in March 2012.','views':100,'likes':100}]
    Business_books  = [
        {'name': 'The First 90 Days, Updated and Expand','description': 'Deals with leadership and career transitions. In this 10th anniversary edition, the author gives you the keys to successfully negotiating your next move - whether you are onboarding into a new company, being promoted internally, or embarking on an international assignment.','views':100,'likes':100},
        {'name': 'One Up on Wall Street: How','description': 'Book De*ion THE NATIONAL BESTSELLING BOOK THAT EVERY INVESTOR SHOULD OWN Peter Lynch is Americas number-one money manager.Hismantra:Average investors can become experts in their own fieldandcanpick winning stocks as effectively as Wall Streetprofessionalsbydoing just a little research.','views':100,'likes':100},
        {'name': 'Howard Marks: The Most Important Thin','description': 'Howard Marks, the chairman and cofounder of Oaktree Capital Management, is renowned for his insightful assessments of market opportunity and risk.','views':100,'likes':100}]
    HealthyMindAndBody_books = [
        {'name': 'Moonwalking with Einstein','description': 'he blockbuster phenomenon that charts an amazing journey of themind while revolutionizing our concept of memory. An instant bestseller that is poised to become a classic','views':100,'likes':100},
        {'name': 'Attached: The New Science of Adult Attachment and How It', 'description': 'Is there a science to love In this groundbreaking book, psychiatrist and neuroscientist Amir Levine and psychologist Rachel S. F. Heller reveal how an understanding of attachment theory-the most advanced relationship science in existence today-can help us find and sustain love.','views':100,'likes':100},
        {'name': 'What is Life?','description': 'Nobel laureate Erwin Schr?dinger’s What is Life is one of the great science classics of the twentieth century.','views':100,'likes':100}]
    CookFoodAndWine_books = [
        {'name': 'A Kitchen in France: A Year of Cooking in My Farmhouse','description': 'With beguiling recipes and sumptuous photography, "A Kitchen in France" transports readers to the French countryside and marks the debut of a captivating new voice in cooking.','views':100,'likes':100},
        {'name': 'The Craft of the Cocktail: Everything You Need to Know to Be','description': 'The first real cookbook for cocktails, featuring 500 recipes from the world’s premier mixologist, Dale DeGroff.Covering the entire breadth of this rich subject','views':100,'likes':100},
        {'name': 'Imbibe! by David Wondrich','description': 'The newly updated edition of David Wondrich s definitive guide to classic American cocktails. Cocktail writer and historian David Wondrich presents the colorful','views':100,'likes':100}]
    HomeAndGarden_books = [
        {'name': 'The World Record Paper Airplane Book','description': 'It s the all you need resources for beginners and experienced paper airplane fliers alike with a total of 20 models and 112 flyers, ready to pull out and fold. But the planes are just the beginning.','views':100,'likes':100},
        {'name': 'the little word of Liz Climo！','description': 'Artist Liz Climo has charmed her fans with her comic world of whimsical animal characters, where everyone from grizzly bears, dinosaurs, rabbits, and anteaters grapple with everyday life with wit and humor.','views':100,'likes':100},
        {'name': ' Urban Dictionary: Freshest Street Slang Defin','description': 'In 1999， Aaron Peckham established UrbanDictionary.com， inviting users to define their world by compiling the most epic collection of slang ever.','views':100,'likes':1000}]

    cats = {'Ficition':{'books': Fiction_books,'likes':10000},
            'Biographies&Memories':{'books': BiographiesAndMemories_books,'likes':1000},
            'Literature':{'books': Literature_books,'likes':1000},
            'Humanities and Social Science':{'books': HumanitiesAndSocialScience_books,'likes':100},
            'TravelGuid':{'books': TravelGuid_books,'likes':1100},
            'ComputerAndInternet':{'books': ComputerAndInternet_books,'likes':1300},
            'Business':{'books': Business_books,'likes':1200},
            'HealthyMind and Body':{'books': HealthyMindAndBody_books,'likes':100},
            'Cook, Food and Wine':{'books': CookFoodAndWine_books,'likes':100},
            'HomeAndGarden':{'books': HomeAndGarden_books,'likes':1400}}

    for cat, cat_data in cats.items():
        c = add_cat(cat,cat_data['likes'])
        for b in cat_data['books']:
            add_book(c, b['name'], b['description'],b['likes'],b['views'])

    # for c in Category.objects.all():
    #     for b in Book.objects.filter(category=c):
    #         print(f'- {c}: {b}')

def add_book(cat, name, description,likes=100,views=70):
    b = Book.objects.get_or_create(category=cat, name=name)[0]
    b.description=description
    b.likes=likes
    b.views=views
    b.save()
    return b

def add_cat(name,likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.likes=likes
    c.save()
    return c

if __name__ == '__main__':
    print('Starting')
    populate()