class Challenge:
    def __init__(self, style, description):
        self.style = style
        self.description = description
    
    def display(self):
        print(description)
        #for time challenges, show either count-down or "Press to stop"
    
    def wait_for_input(self):
        pass  #wait for button, repeat same thing until pressed
    
    def save_results(self):
        pass  #use open to save in unique file (save top 3-5)
    
    def retrieve_results(self):
        pass  #similar to above, but collect old results and print to screen
            #do special effects with buzzer/lights/display if beat records