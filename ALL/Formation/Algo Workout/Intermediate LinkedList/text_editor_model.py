
'''
Text Editor Data Model

We're going to build the data model for a text editor that supports the basic operations needed for typing. This data model will take the form of a class that has methods for:
- typing one character at a time
- backspace and delete to remove text one character at a time
- moving the cursor

How can this class be designed so that the main operations are as efficient as possible?
 

EXAMPLE(S)
const editor = new TextEditor("Text").moveEnd();
console.log(editor.toString(), "Text");
editor.backspace();
console.log(editor.toString(), "Tex");
editor.addChar('t'). addChar(" ").addChar("E").addChar("d").addChar("i").addChar("t");
console.log(editor.toString(), "Text Edit");
editor.moveStart().delete().delete().delete().delete().delete();
console.log(editor.toString(), "Edit");

const e2 = new TextEditor("otter");
console.log(e2.toString(), "otter");
e2.backspace().backspace().backspace().backspace().backspace();
console.log(e2.toString() === "", true);
e2.addChar("a").moveBack().delete();
console.log(e2.toString() === "", true);

 

FUNCTION SIGNATURE
class TextEditor {

  // initialize the editor, optionally with some starter text
  constructor(initialText = "") {
  }

  // remove the character before the cursor
  backspace() {
  }

  // remove the character at the cursor. Cursor moves to the
  // next character.
  delete() {
  }

  // add a new character before the cursor
  addChar(c) {
  }

  // move the cursor back one
  moveBack() {
  }

  // move the cursor forward one
  moveNext() {
  }

  // Move the cursor to the start. A new
  // character added here will be the first.
  moveStart() {
  }

  // move the cursor to the end. A new
  // character here will be last.
  moveEnd() {
  }

  // Return the text currently in the editor as a single string.
  // Can be O(n) in the size of the current text.
  toString() {
  }
  
}

'''
class TextEditor(object):
    class DLNode(object):
        def __init__(self,value='',prev=None,next=None):
            self.value = value 
            self.prev = prev 
            self.next = next 
    
    def __init__(self,initialText=''):
        self.head = TextEditor.DLNode(float('inf'))
        self.tail = TextEditor.DLNode(float('-inf'),self.head)
        self.head.next = self.tail 
        self.cursor = self.tail
        
        for char in initialText:
            self.addChar(char) 
    
    def backspace(self):
        if self.cursor != self.head:
            #affef
            #aff_f
            #afff
            self.cursor.prev = self.cursor.prev.prev
            self.cursor.prev.next = self.cursor 
            self.cursor = self.cursor.prev 
    # affeff 
    def delete(self):
        if self.cursor != self.tail: 
            #affeff
            #    |
            #affe f
            self.cursor.prev.next = self.cursor.next
            self.cursor.next.prev = self.cursor.prev
            self.cursor = self.cursor.next
            
    # 12356
    # 123_56
    # 123456
    def addChar(self,c):
        character_node = TextEditor.DLNode(value=c,next=self.cursor.next,prev=self.cursor)
        self.cursor.next.prev = character_node 
        self.cursor.next = character_node 
        self.cursor = character_node 


    def moveBack(self):
        if self.cursor.prev != self.head:
            self.cursor = self.cursor.prev 
    
    def moveNext(self):
        if self.cursor.next != self.tail: 
            self.cursor = self.cursor.next 
    
    def moveStart(self):
        self.cursor = self.head.next 
    
    def moveEnd(self):
        self.cursor = self.tail.prev 
    
    def toString(self):
        parts = [] 
        curr = self.head.next
        
        while curr != self.tail: 
            parts.append(curr.value)
            curr = curr.next 
        
        return ''.join(parts) 
    
        