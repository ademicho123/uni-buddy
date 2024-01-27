from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# Create the ChatBot instance
chatbot = ChatBot('UniBuddy')


# Train with both ListTrainer and ChatterBotCorpusTrainer
trainer = ListTrainer(chatbot)
trainer.train([
    "How can I access my course materials online?",
    "You can find your course materials on the university's learning management system (LMS).The link and login details should be provided by your instructor.",
    "What academic resources does the university offer to help students succeed?"
    "The university provides resources such as libraries, tutoring services, and study groups to support academic success.",
    "How do I schedule meetings with professors during their office hours?",
    "You can find the professor's office hours on the syllabus or course website. Just drop by during those hours or email to set up an appointment.",
    "What is the process for changing or adding classes?",
    "You can usually make changes to your class schedule during the designated add/drop period. Check with the registrar's office for specific procedures.",
    "Are there opportunities for undergraduate research, and how can I get involved?",
    "Yes, there are often opportunities for undergraduate research. Contact your department or professors to express your interest.",
    "What student organizations are available, and how can I join them?",
    "You can explore a list of student organizations on the university website or attend a student activities fair. Contact the organization directly to join.",
    "Where can I find information about campus events and activities?|Check the university's event calendar, bulletin boards, or follow official social media accounts for updates on campus events.",
    "What recreational facilities are available for students?",
    "Most universities have gyms, sports facilities, and recreational spaces. Check with the campus recreation center for details on access.",
    "How can I get involved in community service or volunteering opportunities?",
    "Contact the university's community service or volunteer center to learn about available opportunities and events.",
    "Are there part-time job opportunities on campus, and how can I apply for them?",
    "Many universities offer part-time job opportunities for students. Check with the campus career center or visit their website for job listings.",
    "How do I apply for on-campus housing, and what are the housing options?",
    "You can apply for on-campus housing through the housing department. They will provide information on available options and the application process.",
    "What dining options are available on campus?",
    "Explore the campus dining services website for information on meal plans, dining locations, and hours of operation.",
    "How can I get a campus ID card, and what is it used for?",
    "You can obtain a campus ID card from the ID card office. It is used for access to facilities, checking out library materials, and more.",
    "Is there a health center on campus, and what services do they provide?",
    "Most universities have a health center that provides basic medical services. Check with them for information on available services and how to make appointments."
    "What transportation options are available for students on and off-campus?",
    "Find information about campus shuttles, public transportation, and parking options for students.",
    "How do I connect to the university's Wi-Fi network?",
    "Information on connecting to the Wi-Fi network should be available on the university's IT website or provided during orientation.",
    "What software is available for students, and how can I access it?"
    "Check with the university's IT department or website for information on available software and how to download or access it.",
    "How can I get technical support for computer issues?",
    "The university's IT helpdesk is there to assist with technical issues. Contact them via phone, email, or visit their office for support.",
    "Is there a computer lab on campus, and what are the hours of operation?",
    "Most campuses have computer labs. Check the university's IT website or ask around for the locations and hours.",
    "Are there any online tutorials or resources for improving my computer skills?",
    "The university's IT department offers online tutorials or direct you to resources for improving your computer skills."
])

