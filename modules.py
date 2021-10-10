class Button():
    extras = None
    def display(self):
        if self.extras[0][0]/self.extras[1][0] <= self.extras[2].mouse.get_pos()[0] <= self.extras[0][0]/self.extras[1][0]+140 and self.extras[0][1]/self.extras[1][1] <= self.extras[2].mouse.get_pos()[1] <= self.extras[0][1]/self.extras[1][1]+40:
            self.extras[2].draw.rect(self.extras[3],self.extras[5],[self.extras[0][0]/self.extras[1][0],self.extras[0][1]/self.extras[1][0],140,40])
        else:
            self.extras[2].draw.rect(self.extras[3],self.extras[4],[self.extras[0][0]/self.extras[1][0],self.extras[0][1]/self.extras[1][0],140,40])
        self.extras[3].blit(self.extras[6].render(self.extras[8] , True , self.extras[7]) , (self.extras[0][0]/10+20,self.extras[0][1]/10+5))
    
    def isClicked(self, event):
        if event.type == self.extras[2].MOUSEBUTTONDOWN:
            if self.extras[0][0]/self.extras[1][0] <= self.extras[2].mouse.get_pos()[0] <= self.extras[0][0]/self.extras[1][0]+140 and self.extras[0][1]/self.extras[1][1] <= self.extras[2].mouse.get_pos()[1] <= self.extras[0][1]/self.extras[1][1]+40:
                return True