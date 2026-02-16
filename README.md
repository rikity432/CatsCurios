# CatsCurios

🐱 Cats Curios
📌 Overview

Cats Curios is a playful yet professional full-stack Django web application that documents the daily adventures of a fictional cat wearing a collar camera. Users can register, interact with posts, and engage in the cat’s daily curiosities.

The project demonstrates full-stack development using:

HTML

CSS

JavaScript

Python

Django

PostgreSQL

Heroku deployment

🎯 Project Goals

Implement full user authentication

Build relational database models

Enable user interaction through comments

Handle image uploads

Deploy to Heroku

Follow Agile methodology

👥 User Stories

Development tracked via GitHub Projects using iterative user stories and MVP-first delivery.

- US18 – User Profile Creation: Users automatically receive a profile when registering.
- US19 – View Profile: Visitors can view profile pages.
- US20 – Edit Profile: Authenticated users can edit their profile.
- US21 – About Page: Visitors can learn about the project and its purpose.

🧱 MVP Features

User registration/login/logout

View all posts

View single post

Comment on posts

User profiles (bio + avatar)

About page

Admin post creation

Image upload support

🛠️ Tech Stack

Django 5.x

PostgreSQL

Gunicorn

Heroku

GitHub

💬 Comment System

Authenticated user commenting

Post–User relational database design

Form validation using Crispy Forms

👤 User Profiles

Extended Django User via a One-to-One `Profile` model.

Automatic profile creation using Django signals.

Editable avatars stored via Cloudinary.

ℹ️ About Page

Provides project context, development goals, and technology overview.

🎨 Wireframes

(Add images here later)

📄 Content Management

Admin-controlled publishing workflow

Comment moderation system

Draft vs published posts

🔎 User Experience Features

Pagination for scalable browsing

Mood-based post filtering

Responsive Bootstrap layout

🛡️ Permissions & Security

Authenticated commenting

Admin-only publishing

Moderated user content

## Features Implemented

- User authentication & profiles
- Admin moderated comments
- AJAX like system
- Mood filtering & pagination
- Cloudinary image uploads
- Interactive Mood Analytics Chart (Chart.js + Django API)
