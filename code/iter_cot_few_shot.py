# this is also for addsub, singleeq, asdiv, svamp
few_shot_4_gsm8k_strong = """Q: Rich likes to take long walks through town. First he walks 20 feet from his house to the sidewalk. Then he walks 200 feet down the sidewalk to the end of the road. Then he makes a left and walks double his total distance so far until he reaches the next intersection. Then he walks half the total distance up to this point again to the end of his route, before turning around and walking the same path all the way back home. How many feet did Rich walk?
A: Reasoning process: 1. Rich walks 20 feet from his house to the sidewalk.
2. He then walks 200 feet down the sidewalk.
3. He makes a left and walks double the distance he had walked so far, or 2 * (20 + 200) = 440 feet.
4. He walks half the distance he had walked up to this point again to the end of his route, or (1/2) * (20 + 200 + 440) = 330 feet.
5. The total distance he walked until the end of his route is 20 + 200 + 440 + 330 = 990 feet.
6. He then walks the same path back home, so the total distance is 2 * 990 = <<2*990=1980>>1980 feet.
Final answer: {1980}.


Q: Patricia is growing her long very long to donate it to a charity that makes wigs for cancer survivors. Her hair is 14 inches long. She needs to donate 23 inches to make a wig. She wants her hair to be 12 inches long after the donation. How much longer does she have to grow her hair?
A: Reasoning process: 1. Patricia needs to donate 23 inches of hair and she currently has 14 inches. So she needs to grow 23-14=9 more inches.
2. After the donation, Patricia wants her hair to be 12 inches long. She will be donating 23 inches, so she will have 12+23=35 inches of hair after the donation.
3. Patricia currently has 14 inches of hair and wants to have 35 inches after the donation. So she needs to grow 35-14=21 more inches.
Thus, Patricia needs to grow her hair 21 more inches to reach her goal. Final answer: {21}.


Q: At the burger hut, you can buy a burger for $5, french fries for $3, and a soft drink for $3.  If you order a special burger meal, you get all 3 of these food items for $9.50. A kid's burger is $3, a kid's french fries are $2, and a kid's juice box is $2.  They also have a kids meal of all 3 kids' food items for $5. Mr. Parker buys 2 burger meals for his wife and himself.  He also buys 2 burger meals and 2 kid's meals for his 4 children.  How much money does Mr. Parker save by buying the 6 meals versus buying the individual food items?
A: Reasoning process: 1. Calculate the cost of a normal burger meal: burger + fries + soft drink = 5 + 3 + 3 = $11
2. Calculate the cost of a special burger meal: $9.50
3. Calculate the cost of a kid's burger meal: kid's burger + kid's fries + kid's juice box = 3 + 2 + 2 = $7
4. Calculate the cost of a special kid's burger meal: $5
5. Calculate the cost of 4 normal burger meals: 4 * 11 = $44
6. Calculate the cost of 4 special burger meals: 4 * 9.50 = $38
7. Calculate the cost of 2 kid's burger meals: 2 * 7 = $14
8. Calculate the cost of 2 special kid's burger meals: 2 * 5 = $10
9. Calculate the total savings: savings on special burger meals + savings on kid's burger meals = 6 + 4 = $10
Final Answer: {10}.


Q: Maurice had only been horseback riding a handful of times in his life. His best friend, Matt, goes horseback riding regularly. When Maurice went to visit Matt for two weeks, he rode another 8 times. Each time, Matt went with him. Meanwhile, besides the times that Matt accompanied Maurice, he rode an additional 16 times. If the total number of times Matt rode during that two weeks is three times the number of times Maurice had ridden before his visit, how many times had Maurice been horseback riding before visiting Matt?
A: Reasoning process: First, we know that Maurice rode 8 times while visiting Matt.
We also know that Matt rode a total of 3 * 8 = 24 times during the two weeks.
We also know that Matt rode an additional 16 times, so his total number of rides during the two weeks was 16 + 24 = 40 times.
We know that Maurice rode a total of 8 + 24 = 32 times during the two weeks.
If the total number of times Matt rode during that two weeks is three times the number of times Maurice had ridden before his visit, we know that 3 * 24 = 72.
Since Maurice rode 8 times during the two weeks, we can say that 8 * 3 = 24 times.
Finally, we know that Maurice had ridden 24 / 3 = 8 times before visiting Matt.
Final answer: {8}.


Q: Kamil wants to renovate his kitchen at home. For this purpose, he hired two professionals who work for him 6 hours a day for 7 days. What does it cost Kamil to hire these professionals if one of them is paid $15 per hour of work?
A: Reasoning process: Kamil hired 2 professionals who work for him for 6 hours a day for 7 days
Each professional works for a total of 6 * 7 = 42 hours
Both professionals work for a total of 42 * 2 = 84 hours
Each professional is paid $15 per hour of work, so the cost for Kamil to hire the professionals is 84 * 15 = $1260
Final answer: {1260}.


Q: Joe played catch with Derek and Tammy. He caught the ball 23 times. Derek made four less than double the catches Joe did. Tammy caught the ball sixteen more than a third of the times Derek did. How many times did Tammy catch the ball?
A: Reasoning process: Joe caught the ball 23 times
Derek caught four less than double the catches Joe did (23 * 2 = 46, 46 - 4 = 42 catches)
Tammy caught 16 more than a third of Derek's catches (42 / 3 = 14, 14 + 16 = 30 catches)
Thus, Tammy caught the ball 30 times. Final answer: {30}.


Q: There are 8 loads of laundry that need to be washed. Each load of laundry takes around 45 minutes to complete in the wash cycle and 1 hour in the dry cycle. How long, in hours, will it take to complete the entire set of laundry?
A: Reasoning process: 1. We need to calculate the time it takes to wash the laundry.
2. We know that there are 8 loads of laundry and that each load takes 45 minutes to wash.
3. Thus, the total time it takes to wash the laundry is 8 loads * 45 minutes/load = 360 minutes.
4. Next, we need to find the time it takes to dry the laundry.
5. We know that it takes 1 hour to dry each load of laundry and that there are 8 loads.
6. Thus, the total time it takes to dry the laundry is 8 loads * 1 hour/load = 8 hours.
7. Finally, we need to add the time it takes to wash and dry the laundry to find the total time it takes to complete the entire set of laundry.
8. To find the total time it takes to complete the laundry, we first need to convert the 360 minutes of washing time to hours.
9. 360 minutes / 60 minutes/hour = 6 hours.
10. Thus, the total time it takes to complete the laundry is 6 hours + 8 hours = 14 hours.
Final answer: {14}.


Q: Bob grew corn in his garden this year and ended up with 50 bushels. This is way too much for him to eat, so he gave some of it away to his friends. His friend Terry took 8 bushels, while Jerry only took 3. He gave 12 bushels to his friend Linda, who runs a food pantry. His neighbor Stacy doesn't eat much corn, but she still accepted 21 ears of corn from him. If each bushel contained 14 ears of corn, how many ears of corn does Bob have left?
A: Reasoning process: First, let's figure out how many bushels of corn Bob gave away to his friends: 8 bushels + 3 bushels + 12 bushels = <<8+3+12=23>>23 bushels of corn.
Next, let's figure out how many ears of corn are in 23 bushels of corn: 23 bushels x 14 ears/bushel = <<23*14=322>>322 ears of corn.
Finally, let's figure out how many ears of corn Bob has left: Bob has 50 bushels of corn, but he gave away 23 bushels and 21 ears, so he has 50 bushels - 23 bushels = 27 bushels of corn left.
Each bushel has 14 ears of corn, so Bob has 27 bushels x 14 ears/bushel = 378 ears of corn left.
The final step is to subtract the 21 ears that Bob gave to Stacy: 378 ears - 21 ears = 357 ears of corn left.
Final answer: {357}."""


few_shot_4_aqua_strong = """Q: A train 360 m long is running at a speed of 45 km/hr. In what time will it pass a bridge 140 m long?
Options: A:40 sec  B:42 sec  C:45 sec  D:48 sec  E:58 sec  
A: Reasoning process: First, we need to calculate the speed of the train in meters per second. We know that 1 hour is equal to 3600 seconds, so the speed of the train in m/s is 45 km/hr * 1000 m/km / 3600 s/hr = 12.5 m/s
Next, we need to find out how long it takes the train to pass the bridge. We know that the length of the train is 360 m, and the length of the bridge is 140 m. So, the time it takes the train to pass the bridge is (140 m + 360 m) / 12.5 m/s = 40 seconds.
Therefore, the correct option is: [A] 40 sec.


Q: In a certain province in Russia there are 15 cities. If a single road segment connects only two cities, how many road segments are required in order to connect the cities so that each city is connected to all other cities with a single road segment?
Options: A:30  B:105  C:330  D:14!  E:15!
A: Reasoning process: First, the first city must be connected to the remaining 14 cities.
This will take 14 road segments.
Next, the second city must be connected to the remaining 13 cities.
This will take 13 road segments.
Finally, the third city must be connected to the remaining 12 cities.
This will take 12 road segments.
This pattern continues until the last city is connected to the remaining 1 city.
This will take 1 road segment.
Therefore, there are a total of 14 + 13 + 12 + ... + 1 = 14 * 15 / 2 = 105 road segments.
The correct option is: [B] 105.


Q: The current of a stream runs at the rate of 4 kmph. A boat goes 6 km and back to the starting point in 2 hours, then find the speed of the boat in still water?
Options: A:6  B:7  C:8  D:5  E:3  
A: Reasoning process: First, let's assume that the speed of the boat in still water is x km/hr.
Since the current of the stream is 4 km/hr, the boat travels 6 km downcurrent in 6 km / (4 km/hr + x km/hr) hours.
Similarly, the boat travels 6 km against the current in 6 km / (x km/hr - 4 km/hr) hours.
Adding these two times, we find that the total time the boat spends traveling downcurrent and against the current is 2 hours.
Solving for x, we find that the boat speed in still water is 8 km/hr.
Therefore, the correct option is: [C] 8.


Q: A car is running at a speed of 96kmph. What distance will it cover in 14sec?
Options: A:378m  B:350m  C:380m  D:200m  E:250m
A: Reasoning process: 1. We are given that the car is running at a speed of 96 km per hour.
2. We want to find the distance it will cover in 14 seconds.
3. We need to convert both km and hours to meters and seconds in order to compare them.
4. 1 hour has 60 minutes, 1 minute has 60 seconds, so 1 hour has 3600 seconds.
5. 1 km has 1000 meters, so 96 km have 96*1000 = 96000 meters.
6. Since we are given the speed of the car in km per hour, we need to divide the total distance in meters by the total time in seconds to find the distance in meters per second.
7. So, the distance the car will cover in 14 seconds is 96000 meters / 3600 seconds/hour * 14 seconds = 378.89 meters.
Final answer: The distance the car will cover in 14 seconds is [A]378m.
Therefore, the correct option is: [A]."""


few_shot_4_commonsense_strong = """Q: Where can peanut butter be stored? Choices: A.container   B.supermarket   C.pantry   D.sandwich   E.jar
A: Reasoning process: 1. Peanut butter is a food item.
2. Food items are usually stored in a place where they can stay fresh, like a refrigerator or a pantry.
3. A pantry is a good option for storing food items that don't need to be refrigerated, like peanut butter.
Therefore, the correct answer is: [C. pantry]


Q: He waited for his friend at the squash court, but he was worried his friend thought he meant the at the other end of the public what? Choices: A.country club   B.rich person's house   C.pool   D.park   E.fitness center
A: Reasoning process: The person is waiting at a squash court, so they are likely at a sports facility or gym.
Out of the options given, the only option that seems like it could be at the other end of a public place is a park.
Therefore, the correct answer is: [D. park]


Q: What do people want to do when they love a place that they are going on vacation in? Choices: A.pleasant thoughts   B.overspending   C.moving there   D.staying there   E.debt
A: Reasoning process: 1. People want to do something when they love a place that they are going on vacation in.
2. The options given are A. pleasant thoughts, B. overspending, C. moving there, D. staying there, and E. debt.
3. Out of these options, the only one that makes sense as something people might want to do when they love a place is D. staying there.
Therefore, the correct answer is: [D. staying there]


Q: Where can meat last a long time? Choices: A.backery   B.ham sandwich   C.fridge   D.butcher shop   E.freezer
A: Reasoning process: Meat is something that can spoil quickly, so we need to find a place that can keep it fresh and prevent it from going bad.
A backery is not a good place for keeping meat because it is usually warm and not refrigerated, which is not good for keeping meat fresh.
A ham sandwich is not a good place for keeping meat because it is already made and ready to eat, so the meat is already exposed to the air and will go bad quickly.
A fridge is a good place for keeping meat because it is cold and refrigerated, which is ideal for keeping meat fresh and preventing it from going bad.
A butcher shop is not a good place for keeping meat because it is usually warm and not refrigerated, which is not good for keeping meat fresh.
A freezer is also a good place for keeping meat because it is very cold and can keep the meat frozen, which prevents it from going bad and can last a long time.
The other choices are not good places for keeping meat because they are not cold enough or not designed for storing meat. As a freezer includes a fridge, it is the best option for keeping meat fresh and preventing it from going bad.
Therefore, the correct answer is: [E. freezer].


Q: What does someone living life fully feel? Choices: A.joy   B.valuable   C.happiness   D.early death   E.adventurous
A: Reasoning process: 1. To understand what it means to live life fully, we need to consider that it could mean living life to the fullest or experiencing all aspects of life and making the most of every moment.
2. Based on this understanding, we need to think about the emotions and feelings that someone who is living life fully might experience.
3. Joy and happiness are positive emotions that align with the idea of living life fully.
4. Other options like early death, valuable, and adventurous are not emotions or feelings and do not align with the idea of living life fully.
5. Therefore, the correct answer is either [A. joy] or [C. happiness]. Final Answer: [A. joy] is probably the better answer as it is more specific and relates more closely to the idea of living life fully.  So, the correct answer is: [A. joy] 


Q: Sky diving scared him, once they jumped out of the plane he began losing consciousness while what? Choices: A.injury   B.death   C.playing uno   D.coma   E.falling down
A: Reasoning process: Sky diving scared him: This means he was afraid of sky diving.
Once they jumped out of the plane: This means they were in the plane, but then they jumped out.
He began losing consciousness: This means he was losing consciousness, or becoming unconscious.
While what? This means we need to figure out what was happening while he was losing consciousness.
Final answer: From the given choices, the only one that makes sense in this context is option E, falling down. Falling down is the natural result of jumping out of a plane, and it could potentially cause someone to lose consciousness.
Therefore, the correct answer is: [E] falling down.


Q: The wood became fossilized, what did the paleontologists call it when they found ti? Choices: A.sanded   B.composted   C.warp   D.hardened   E.petrify
A: Reasoning process: First, we need to understand what fossilization is. Fossilization is the process by which an organism is preserved in the fossil record. This can happen through a variety of processes, such as being buried in sediment, being exposed to high pressures and temperatures, or being replaced by minerals.
Now let's look at the options given. We know that wood is a type of organism, so if it became fossilized, it would be preserved in the fossil record. We also know that the wood would have undergone some kind of process to become fossilized, such as being buried in sediment or being exposed to high temperatures and pressures.
Option A, "sanded," doesn't really make sense. Sanding is a process used to smooth wood or other materials, but it wouldn't have anything to do with fossilization.
Option B, "composted," also doesn't really make sense. Composting is the process of breaking down organic matter into a nutrient-rich soil amendment, but it wouldn't have anything to do with fossilization.
Option C, "warp," doesn't really make sense either. Warping is a term used to describe wood that has been bent or twisted out of shape, but it wouldn't have anything to do with fossilization.
Option D, "hardened," is a possibility. Hardening is a process that can happen to wood or other materials over time, as they become more dense and resistant to damage. This could be a possible outcome of the fossilization process, but it's not the only possibility.
Option E, "petrify," is the correct answer. Petrify means to turn into stone or a stony substance, which is exactly what happens to wood during the fossilization process. The wood becomes preserved in the fossil record, and is replaced by minerals over time. This process is called petrification, and the resulting fossil is called a petrified wood fossil.
So the correct answer is: [E. petrify]."""

few_shot_4_date_strong = """Q: This is the last day of 1899. What is the date today in MM/DD/YYYY? Choices: A.09/26/1899 B.12/31/1899 C.11/30/1899 D.01/09/1900 E.12/22/1899 F.12/31/1885
A: Reasoning process: 1. The year is 1899 because it is the last day of the year.
2. The month is December because it is the last day of the month.
3. The date is 31 because it is the last day of the month.
Therefore, the correct answer is: {B.12/31/1899}


Q: Today is the palindrome day of 2020, because the MMDDYYYY format of the date is the same backwards as forwards. What is the date 24 hours later in MM/DD/YYYY? Choices: A.02/03/1982 B.02/03/2100 C.02/03/2020 D.02/04/2020 E.02/03/2094 F.01/02/2020
A: Reasoning process: 1. The date is 02/02/2020, because the MMDDYYYY format of the date is the same backwards as forwards.
2. The date 24 hours later is 02/03/2020, because we add 24 hours to the date and the date changes to the next day.
Final answer: {C:02/03/2020}.


Q: This is the last day of 1899. What is the date today in MM/DD/YYYY? Choices: A.09/26/1899 B.12/31/1899 C.11/30/1899 D.01/09/1900 E.12/22/1899 F.12/31/1885
A: Reasoning process: 1. We know that this is the last day of 1899, so the year must be 1899.
2. We need to find the date today in MM/DD/YYYY format.
3. Based on the given information, the date must be December 31, 1899.
4. Therefore, the answer is 12/31/1899.
Final answer: {B.12/31/1899}


Q: Yesterday was 12/31/1929. Today could not be 12/32/1929 because December has only 31 days. What is the date today in MM/DD/YYYY? Choices: A.10/01/1930 B.12/31/1929 C.02/27/1930 D.01/06/1930 E.01/01/1930 F.01/08/1930
A: Reasoning process: Yesterday is 12/31/1929. We know that December has 31 days. This means that yesterday is the last day in December.
Today is not 12/32/1929, because December only has 31 days. This means that today is not December.
Since yesterday was the last day in December, today must be the first day in a new month.
The next month after December is January, so today must be 01/01/1930.
Final answer: {E}


Q: The current local time is 3:02 pm of 5/4/2004. What is the date tomorrow in MM/DD/YYYY? Choices: A.05/05/1915 B.05/06/2004 C.01/05/2005 D.05/04/2004 E.02/15/2004 F.05/05/2004
A: Reasoning process: 1. Since it's currently 3:02 pm, we know that the time tomorrow will be 3:02 pm, or 15:02.
2. Since the date today is 5/4/2004, we can add one day to get 5/5/2004.
3. Therefore, the correct answer is: {F.05/05/2004}.


Q: Today is the second day of the third month of 1966. What is the date tomorrow in MM/DD/YYYY? Choices: A.03/02/1966 B.03/04/1966 C.03/24/1966 D.03/03/1966 E.02/28/1966
A: Reasoning process: First, we need to find the month of tomorrow's date. We know that the current month is the third month, so we add 1 to get the next month, which is the fourth month.
Second, we need to find the day of tomorrow's date. We know that today is the second day of the month, so we add 1 to get the next day, which is the third day.
Third, we need to find the year of tomorrow's date. We know that the current year is 1966, and since the current month is March and we are moving to the next month, the year does not change.
Final answer: {03/03/1966}.


Q: Today is Sep 9, 1909. What is the date today in MM/DD/YYYY? Choices: A.09/09/1939 B.12/11/1909 C.09/09/1909 D.09/30/1909 E.11/19/1909 F.09/09/1886
A: Reasoning process: Today is Sep 9, 1909. The year is 1909, so the date is 09/09/1909
The correct answer is: {09/09/1909}


Q: Jane visits the bookstore on the 16th of each month starting from the October of 2009. It is her 5th visit to the bookstore today. What is the date tomorrow in MM/DD/YYYY? Choices: A.02/17/2010 B.02/16/2010 C.11/17/2009 D.02/14/2010 E.02/26/2010 F.02/17/2096
A: Reasoning process: 1. Jane visits the bookstore on the 16th of each month.
2. It is her 5th visit to the bookstore today.
3. We know that the date today is the 16th of the month.
4. We know that the date tomorrow is the 17th of the month.
Final answer: The correct answer is {B.02/16/2010}."""

few_shot_4_object_strong = """Q: Alice, Bob, and Claire are on the same team in a soccer match. At the start of the match, they are each assigned to a position: Alice is playing cheerleader, Bob is playing right winger, and Claire is playing goalkeeper. As the game progresses, pairs of players occasionally swap positions. First, Alice and Claire trade positions. Then, Bob and Alice trade positions. Finally, Claire and Bob trade positions. At the end of the match, Claire is playing? Choices: A.cheerleader. B.right winger. C.goalkeeper.
A: Reasoning process: At the start of the match, Alice is playing cheerleader, Bob is playing right winger, and Claire is playing goalkeeper.
In the first swap, Alice and Claire trade positions, so Alice is now playing goalkeeper and Claire is now playing cheerleader.
In the second swap, Bob and Alice trade positions, so Bob is now playing goalkeeper and Alice is now playing right winger.
In the third and final swap, Claire and Bob trade positions, so Claire is now playing goalkeeper and Bob is now playing cheerleader.
Therefore, the final answer is: {goalkeeper}.


Q: Alice, Bob, and Claire are playing a game. At the start of the game, they are each holding a ball: Alice has a white ball, Bob has a purple ball, and Claire has a pink ball. As the game progresses, pairs of players trade balls. First, Bob and Alice swap balls. Then, Bob and Claire swap balls. Finally, Bob and Alice swap balls. At the end of the game, Claire has the? Choices: A.white ball. B.purple ball. C.pink ball.
A: Reasoning process: At the start of the game, Alice has a white ball, Bob has a purple ball, and Claire has a pink ball. Then, Bob and Alice swap balls, so now Alice has a purple ball and Bob has a white ball. Then, Bob and Claire swap balls, so now Bob has a pink ball and Claire has a white ball. Finally, Bob and Alice swap balls again, so now Bob has a white ball and Alice has a pink ball. At the end of the game, Claire has the white ball. Answer: {A}.


Q: Alice, Bob, and Claire are holding a white elephant gift exchange. At the start of the event, they are each holding a present of a different color: Alice has a yellow present, Bob has a purple present, and Claire has a green present. As the event progresses, pairs of people swap gifts. First, Claire and Alice swap their gifts. Then, Bob and Claire swap their gifts. Finally, Alice and Bob swap their gifts. At the end of the event, Alice has the? Choices: A.yellow present. B.purple present. C.green present.
A: Reasoning process: At the start, Alice has a yellow present, Bob has a purple present, and Claire has a green present.
After the first swap, Alice has a green present, Bob has a purple present, and Claire has a yellow present.
After the second swap, Alice has a green present, Bob has a yellow present, and Claire has a purple present.
Finally, after the third swap, Alice has a yellow present and Bob has a purple present.
Final answer: {A.yellow present.}


Q: Alice, Bob, and Claire are playing a game. At the start of the game, they are each holding a ball: Alice has a brown ball, Bob has a pink ball, and Claire has a blue ball. As the game progresses, pairs of players trade balls. First, Claire and Bob swap balls. Then, Claire and Alice swap balls. Finally, Bob and Claire swap balls. At the end of the game, Bob has the? Choices: A.pink ball. B.brown ball. C.blue ball.
A: Reasoning process: At the start of the game, Alice has a brown ball, Bob has a pink ball, and Claire has a blue ball.
After the first swap, Claire and Bob swap balls. So Claire now has a pink ball and Bob has a blue ball.
After the second swap, Claire and Alice swap balls. So Claire now has a brown ball and Alice has a pink ball.
Finally, Bob and Claire swap balls. So Bob now has a brown ball and Claire has a blue ball.
Therefore, the correct answer is: {B.brown ball.}


Q: Alice, Bob, and Claire are playing a game. At the start of the game, they are each holding a ball: Alice has a orange ball, Bob has a white ball, and Claire has a pink ball. As the game progresses, pairs of players trade balls. First, Claire and Alice swap balls. Then, Bob and Alice swap balls. Finally, Alice and Claire swap balls. At the end of the game, Claire has the? Choices: A.pink ball. B.orange ball. C.white ball.
A: Reasoning process: At the start of the game, Claire has a pink ball, Alice has an orange ball, and Bob has a white ball.
In the first trade, Claire and Alice swap balls. So now, Claire has an orange ball, Alice has a pink ball, and Bob has a white ball.
In the second trade, Bob and Alice swap balls. So now, Claire has an orange ball, Alice has a white ball, and Bob has a pink ball.
In the third trade, Alice and Claire swap balls again. So now, Claire has a white ball, Alice has an orange ball, and Bob has a pink ball.
Therefore, the correct answer is: {C.white ball.}


Q: Alice, Bob, and Claire are holding a white elephant gift exchange. At the start of the event, they are each holding a present of a different color: Alice has a green present, Bob has a red present, and Claire has a purple present. As the event progresses, pairs of people swap gifts. First, Bob and Claire swap their gifts. Then, Claire and Alice swap their gifts. Finally, Alice and Bob swap their gifts. At the end of the event, Alice has the? Choices: A.red present. B.green present. C.purple present.
A: Reasoning process: At the start of the event, Alice has a green present, Bob has a red present, and Claire has a purple present. After the first swap, Bob has the purple present and Claire has the red present. After the second swap, Claire has the green present and Alice has the red present. After the final swap, Alice has the purple present and Bob has the red present. the correct answer is: {C.purple present}.


Q: Alice, Bob, and Claire are on the same team in a soccer match. At the start of the match, they are each assigned to a position: Alice is playing striker, Bob is playing center midfielder, and Claire is playing left midfielder. As the game progresses, pairs of players occasionally swap positions. First, Claire and Bob trade positions. Then, Claire and Alice trade positions. Finally, Bob and Claire trade positions. At the end of the match, Claire is playing? Choices: A.center midfielder. B.striker. C.left midfielder.
A: Reasoning process: First, Claire and Bob trade positions, so Claire is now the center midfielder. Then, Claire and Alice trade positions, so Claire is now the striker. Finally, Bob and Claire trade positions, so Claire is now the left midfielder. Therefore, the correct answer is: {C.left midfielder}.


Q: Alice, Bob, and Claire are holding a white elephant gift exchange. At the start of the event, they are each holding a present of a different color: Alice has a white present, Bob has a pink ball, and Claire has a black ball. As the event progresses, pairs of people swap gifts. First, Alice and Claire swap their gifts. Then, Alice and Bob swap their gifts. Finally, Claire and Alice swap their gifts. At the end of the event, Alice has the? Choices: A.pink ball. B.white present. C.black ball.
A: Reasoning process: At the start of the event, Alice has a white present and Claire has a black ball.
After the first swap, Alice has a black ball and Claire has a white present.
After the second swap, Alice has a pink ball and Bob has a black ball.
After the third swap, Alice has a white present and Claire has a pink ball.
Therefore, the correct answer is: {B.white present}."""

few_shot_4_lastletter_strong = """Q: Take the last letters of the words in "Herbert Tapia" and concatenate them.
A: Reasoning process: To get the last letters of the words in "Herbert Tapia," we need to first find the last letter of each word. For the word "Herbert," the last letter is "t." For the word "Tapia," the last letter is "a." Next, we need to concatenate these two letters to get our final answer. To concatenate two strings, we simply put them together in the order we want them. Final answer: {ta}.


Q: Take the last letters of the words in "Parker Nunez" and concatenate them.
A: Reasoning process: First, we need to take the last letters of the words in "Parker Nunez". These are "r" and "z". Then, we need to concatenate these letters to get our final answer. Final answer: rz. the correct answer is: {rz}


Q: Take the last letters of the words in "Raymond Avery" and concatenate them.
A: Reasoning process: 1. First, we need to find the last letters of the words in "Raymond Avery".
2. So, we need to find the last letters of "Raymond" and "Avery".
3. The last letters of "Raymond" and "Avery" are "d" and "y", respectively.
4. Now, let's concatenate these letters.
Final answer: {dy}

Q: Take the last letters of the words in "Yong Hogan" and concatenate them.
A: Reasoning process: 1. We need to take the last letters of the words in "Yong Hogan". 2. Let's identify the words in "Yong Hogan". We have two words: "Yong" and "Hogan". 3. Let's take the last letters of each word. The last letter of "Yong" is "g" and the last letter of "Hogan" is "n". 4. When we concatenate the last letters, we get "gn". Final answer: the correct answer is: {gn}."""


few_shot_4_gsm8k_weak =""""""
few_shot_4_aqua_weak =""""""
few_shot_4_commonsenseqa_weak =""""""
few_shot_4_strategyqa_weak =""""""
few_shot_4_date_weak =""""""
few_shot_4_object_weak =""""""
few_shot_4_lastletter_weak =""""""