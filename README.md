
## Inspiration
The theme posed quite a challenge to come up with up a testable idea, since I had never had any pets, I wanted to make sure that my project had an accessibility component for our furry friends with hearing or sigh challenges, since there are no such solutions out there yet!

We know that dogs are smart, but they cannot articulately express their needs to us, as they cannot speak human language. This projects attempts to create an easy-to-use interface which dogs(with or without hearing/sight challenges) can be trained to use to talk to us in a better way. Similarly, dog owners with hearing/speaking/sight challenges can interact with their pets in a new way.

## What it does
This prototype facilitates higher-quality communication between pets and their owners, whether or not they have challenges, by presenting an interface of 6 buttons, all programmed to convey specific phrases. There is a speaker connected to the system, which says these phrases when a specific button is pressed, to help our owners and pets with sigh challenges. There is also an OLED screen which visually displays these phrases to make this solution accessible to owners and pets with hearing challenges. 

![OLED screen showing a visualization of "Good dog!"](https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/002/253/959/datas/original.jpg)
Additionally, there is a mechanism to switch between dog to human communication and human to dog communication.

Here are the in-built phrases a dog can be trained to say:
* Yes
* No
* Can I have a treat?
* I need to go to the bathroom
* Can we go outside for a walk?
* I'm hungry. Can I get some food?

Here are the in-built phrases an owner can say to a dog. These include some specific commands that guide dogs around the world understand:

* Come here
* Good Dog!
* Leave it (to correct a dog when it's doing something it shouldn't)
* Wait
* Okay (to tell a dog it is temporarily relieved of duty)
* Call another human for help

When a human presses the button to ask their dog to call another human for help, the system also sends an automated SMS message to a preset emergency contact using Twilio. 
![The spread of buttons](https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/002/253/957/datas/original.jpg)

Additionally, if there is something an owner wants to say which is not given on the buttons, they can go to [dogtalk.tech](http://dogtalk.tech) and enter what they want to say.
![dogtalk.tech](https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/002/254/177/datas/original.png)Once the owner clicks "Submit", the system will convert the text to speech and say it through the speaker.


## How we built it
The heart of the system is a Raspberry Pi 4 and the following components:
* 6 momentary push buttons
* 128x64 monochrome OLED screen
* SPDT switch

There are pre-recorded sounds containing the pre-determined phrases on the local filesystem, and they are played using pygame based on the which button and pressed and the selection of the SPDT switch. 

Similarly, there are pre-loaded images representing each pre-determined phrase, which are displayed on the OLED screen based on the which button and pressed and the selection of the SPDT switch. The OLED screen is flipped based on the SPDT switch selection, as it is assumed that the dog and owner will be on opposite sides on the device.

![A button](https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/002/253/960/datas/gallery.jpg)

Each button is basically a piece of styrofoam covered with paper with a momentary push button attached underneath.

The SMS functionality of the "Help" button uses Twilio to send an automated text message to a predetermined user, which in this is my personal number. Here is the message that we receive in the video:


![The text message](https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/002/253/958/datas/gallery.jpg)


The website [dogtalk.tech](https://dogtalk.tech) is hosted on **GitHub pages**, and the domain (http://dogtalk.tech) was procured from **Domain.com**. This website takes some text, sends to the Raspberry Pi, which then uses the gTTS API to convert the text to speech and play it.

Playing audio uses the pygame module, and the OLED screen is controlled using Adafruit modules. Ideally, the OLED screen would be bigger, so that it can easily be seen from a distance, but I only had this one.

## Challenges we ran into
* Since I don't really have experience with web development, it was a major challenge for me to create an online interface for the text to speech functionality. The main issue was transferring some text to the Raspberry Pi without having to create a whole new server, and making the project too complex. Ultimately this was solved by transferring the data to Firebase using HTTP requests, and then Firebase streaming this data real time to the Raspberry Pi.
* I wanted to make the website look a little better than plain HTML, so it took me a lot of fiddling with bootstrap to get it to look better.

## Accomplishments that we're proud of
* Finding a way to transfer data from GitHub pages to the Raspberry Pi.
* Creating a project that helps dogs with accessibility needs, along with humans with accessibility needs.  
* Completing the project in time, as I was working solo.

## What we learned
* Twilio integration - this was particularly time consuming and tedious
* AJAX - used to dynamically work with pages
* How to receive HTML form data in JavaScript

## What's next for DogTalk
* Adding animations to the OLED screen to better represent specific phrases.
* Adding a bigger screen for visualization.
* Dog-proofing the design.
