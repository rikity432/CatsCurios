# CatsCurios

A playful Django web application documenting the daily adventures of a curious cat through blog-style entries, interactive reactions, and live community features.

Live Site: (https://catscurios-aa2feb00a994.herokuapp.com/)
Repository: (https://github.com/rikity432/CatsCurios)

📖 Project Overview

Cats Curios is a full-stack Django application built as a final capstone project during a 16-week programming skills bootcamp.

The platform allows users to follow a fictional cat’s daily experiences, interact through comments and reactions, and participate in a live chat environment.

The project demonstrates modern full-stack development practices including authentication, database design, AJAX interactions, and deployment.

🎯 Project Goals

Build a full CRUD Django application

Implement authentication & user profiles

Demonstrate relational database design

Use AJAX for dynamic UI updates

Deploy a production-ready application

✨ Features
Core Features

Admin-created blog posts

User registration & login

User profiles with images

Comment system with admin approval

Mood filtering & pagination

Interactive Features

AJAX like/reaction system

Live chat with profanity filtering

Cat status indicator (dynamic navbar)

Online users tracker

Mood analytics chart (Chart.js)

🧱 Technology Stack
Frontend

HTML5

CSS3

Bootstrap

JavaScript (AJAX)

Chart.js

Backend

Python

Django

PostgreSQL

Deployment & Tools

Heroku

Cloudinary

GitHub

Crispy Forms

🗄 Database Design
Entity Relationship Diagram

(paste Mermaid ERD here)

🧠 Agile Development

Project planning followed Agile principles:

User stories tracked via GitHub Projects

Iterative feature delivery

MVP-first development approach

Example User Story:

As a user, I can like a post so that I can react to the cat’s adventures.

🚀 Deployment

Application deployed using Heroku:

PostgreSQL database configured

Cloudinary media storage enabled

Environment variables secured

Static files collected via WhiteNoise

🧪 Testing

Manual testing performed across:

Authentication flows

Comment moderation

AJAX interactions

Mobile responsiveness

🔮 Future Improvements

WebSocket real-time chat

Follow favourite users

Cat achievement badges

Notification system

👨‍💻 Author

Created as a capstone portfolio project demonstrating Django full-stack development skills.

Background image from: <a href="https://www.freepik.com/free-vector/modern-abstract-dark-violate-pink-background_159480816.htm#fromView=keyword&page=1&position=1&uuid=3eb7d263-64db-414b-93b0-d8ffce92635c&query=Modern+background">Image by muhammad.abdullah on Freepik</a>


```mermaid
erDiagram

    User ||--|| Profile : has
    User ||--o{ Comment : writes
    User ||--o{ Reaction : likes
    User ||--o{ ChatMessage : sends

    Post ||--o{ Comment : receives
    Post ||--o{ Reaction : receives

    User {
        int id PK
        string username
        string email
        string password
    }

    Profile {
        int id PK
        int user_id FK
        string bio
        string profile_image
        datetime last_seen
    }

    Post {
        int id PK
        string title
        text content
        string mood
        image featured_image
        datetime created_on
        boolean approved
    }

    Comment {
        int id PK
        int user_id FK
        int post_id FK
        text body
        boolean approved
        datetime created_on
    }

    Reaction {
        int id PK
        int user_id FK
        int post_id FK
        datetime created_on
    }

    ChatMessage {
        int id PK
        int user_id FK
        text message
        datetime created_at
    }
```