f = open("html.txt","w")

for i in range(1,12):
    f.write(f'<a class="spotlight" href="images/salzburg/salzburg1({i}).jpg"><img src="images/salzburg/salzburg1({i}).jpg" class="ag-timeline-card_img" alt="" style="display: none;"/></a>\n')
