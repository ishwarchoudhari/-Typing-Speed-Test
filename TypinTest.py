def run(self):
    self.reset_game()
    self.running=True
    while(self.running):
        clock = pygame.time.Clock()
        self.screen.fill((0,0,0), (50,250,650,50))
        pygame.draw.rect(self.screen,self.HEAD_C, (50,250,650,50), 2)
        # update the text of user input
        self.draw_text(self.screen, self.input_text, 274, 26,(250,250,250))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                x,y = pygame.mouse.get_pos()
                # position of input box
                if(x>=50 and x<=650 and y>=250 and y<=300):
                    self.active = True
                    self.input_text = ''
                    self.time_start = time.time()
                 # position of reset box
                 if(x>=310 and x<=510 and y>=390 and self.end):
                    self.reset_game()
                    x,y = pygame.mouse.get_pos()
            elif event.type == pygame.KEYDOWN:
                if self.active and not self.end:
                    if event.key == pygame.K_RETURN:
                        print(self.input_text)
                        self.show_results(self.screen)
                        print(self.results)
                        self.draw_text(self.screen, self.results,350, 28, self.RESULT_C)
                        self.end = True
                    elif event.key == pygame.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]
                    else:
                        try:
                            self.input_text += event.unicode
                        except:
                            pass
        pygame.display.update()
    clock.tick(60
