#Base Class - Instagram Story
class InstagramStory:
    def __init__(self, user):
        self.user = user
        print(f"\n {self.user} user is created.")
        self.story_content = ""

    def post_story(self, content):
        self.story_content = content
        print( f"{self.user} posted a story: {content}")

#Single Inheritance - Adds Like Feature

class StoryWithLikes(InstagramStory):
    def __init__(self, user):
        super().__init__(user)
        self.likes = 0

    def like_story(self):
        self.likes += 1
        print( f"Story liked! Total likes: {self.likes}")

#Single Inheritance - Adds Comments Feature separately
class StoryWithComments(InstagramStory):
    def __init__(self, user):
        super().__init__(user)
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)
        print(f"New comment added: {comment}")

#Hierarchical Inheritance - Adds Reaction Feature
class StoryWithReactions(InstagramStory):
    def __init__(self, user):
        super().__init__(user)
        self.reactions = {"😂": 0, "❤": 0, "🔥": 0}

    def react_to_story(self, reaction):
        if reaction in self.reactions:
            self.reactions[reaction] += 1
            print( f"Reaction {reaction} added! Total: {self.reactions[reaction]}")
        else:
            print( "Invalid reaction!")

#Multiple Inheritance - Combines Likes, Comments, Reactions + Close Friends Feature
class StoryWithCloseFriends(StoryWithLikes, StoryWithComments, StoryWithReactions):
    def __init__(self, user):
        StoryWithLikes.__init__(self, user)  
        StoryWithComments.__init__(self, user)
        StoryWithReactions.__init__(self, user)
        self.close_friends_only = False

    def set_close_friends(self, status):
        self.close_friends_only = status
        mode = "Close Friends" if status else "Public"
        print( f"Story visibility set to: {mode}")

print("\nSiva")
siva=InstagramStory("Siva")
siva.post_story("sunday is holiday")

print("\Kowshik")
kowshik=StoryWithLikes("Kowshik")
kowshik.post_story("Monday is Holiday")
kowshik.like_story()
kowshik.like_story()
kowshik.like_story()
kowshik.like_story()

print("\n Rasool")
rasool=StoryWithComments("Rasool")
rasool.post_story("Tuesday is holiday")
rasool.add_comment("It's is wrong.")


print("\n Kiran")
kiran=StoryWithReactions("Kiran")
kiran.post_story("Wednesday is Holiday")
kiran.react_to_story("😂")
kiran.react_to_story("❤")
kiran.react_to_story("😂")
kiran.react_to_story("❤")
kiran.react_to_story("😂")
kiran.react_to_story("🔥")

print("\n Manju")
manju=StoryWithCloseFriends("Manju")
manju.post_story("Saturday is Holiday")
manju.post_story("Monday is Holiday")
manju.like_story()
manju.like_story()
manju.like_story()
manju.like_story()
manju.react_to_story("😂")
manju.react_to_story("❤")
manju.react_to_story("😂")
manju.react_to_story("❤")
manju.react_to_story("😂")
manju.react_to_story("🔥")
manju.set_close_friends("Yes")

'''

Output :


Siva

 Siva user is created.
Siva posted a story: sunday is holiday
\Kowshik

 Kowshik user is created.
Kowshik posted a story: Monday is Holiday
Story liked! Total likes: 1
Story liked! Total likes: 2
Story liked! Total likes: 3
Story liked! Total likes: 4

 Rasool

 Rasool user is created.
Rasool posted a story: Tuesday is holiday
New comment added: It's is wrong.

 Kiran

 Kiran user is created.
Kiran posted a story: Wednesday is Holiday
Reaction 😂 added! Total: 1
Reaction ❤ added! Total: 1
Reaction 😂 added! Total: 2
Reaction ❤ added! Total: 2
Reaction 😂 added! Total: 3
Reaction 🔥 added! Total: 1

 Manju

 Manju user is created.

 Manju user is created.

 Manju user is created.
Manju posted a story: Saturday is Holiday
Manju posted a story: Monday is Holiday
Story liked! Total likes: 1
Story liked! Total likes: 2
Story liked! Total likes: 3
Story liked! Total likes: 4
Reaction 😂 added! Total: 1
Reaction ❤ added! Total: 1
Reaction 😂 added! Total: 2
Reaction ❤ added! Total: 2
Reaction 😂 added! Total: 3
Reaction 🔥 added! Total: 1
Story visibility set to: Close Friends
'''