

def bug_log(text):
    f = open("bug_log.txt", "a")
    f.write(text +"\n")
    f.close()

def make_msg(text, user, userid):
    output = "From user "+ user + " with id " + str(userid)
    output+= "\n" + text + "\n"
    return output


bug_log("TEST")