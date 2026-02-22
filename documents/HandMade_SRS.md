# Software Requirements Specification (SRS)
## For
# Hand Made (Aap ki dukaan)

**Version:** 2.0
**Prepared by:** Antigravity
**Date:** 2025-11-26

---

## Table of Contents

1. [Introduction](#1-introduction)
    1.1 [Purpose](#11-purpose)
    1.2 [Document Conventions](#12-document-conventions)
    1.3 [Intended Audience and Reading Suggestions](#13-intended-audience-and-reading-suggestions)
    1.4 [Product Scope](#14-product-scope)
    1.5 [References](#15-references)
2. [Overall Description](#2-overall-description)
    2.1 [Product Perspective](#21-product-perspective)
    2.2 [Product Functions](#22-product-functions)
    2.3 [User Classes and Characteristics](#23-user-classes-and-characteristics)
    2.4 [Operating Environment](#24-operating-environment)
    2.5 [Design and Implementation Constraints](#25-design-and-implementation-constraints)
    2.6 [User Documentation](#26-user-documentation)
    2.7 [Assumptions and Dependencies](#27-assumptions-and-dependencies)
3. [System Architecture](#3-system-architecture)
    3.1 [Architectural Design](#31-architectural-design)
    3.2 [Module Decomposition](#32-module-decomposition)
    3.3 [Database Design](#33-database-design)
4. [External Interface Requirements](#4-external-interface-requirements)
    4.1 [User Interfaces](#41-user-interfaces)
    4.2 [Hardware Interfaces](#42-hardware-interfaces)
    4.3 [Software Interfaces](#43-software-interfaces)
    4.4 [Communications Interfaces](#44-communications-interfaces)
5. [System Features (Functional Requirements)](#5-system-features-functional-requirements)
    5.1 [User Authentication Module](#51-user-authentication-module)
    5.2 [Product Management Module](#52-product-management-module)
    5.3 [Shopping Cart Module](#53-shopping-cart-module)
    5.4 [Search and Filtering Module](#54-search-and-filtering-module)
    5.5 [User Dashboard Module](#55-user-dashboard-module)
6. [Other Nonfunctional Requirements](#6-other-nonfunctional-requirements)
    6.1 [Performance Requirements](#61-performance-requirements)
    6.2 [Safety Requirements](#62-safety-requirements)
    6.3 [Security Requirements](#63-security-requirements)
    6.4 [Software Quality Attributes](#64-software-quality-attributes)
    6.5 [Business Rules](#65-business-rules)
7. [Testing Strategy](#7-testing-strategy)
    7.1 [Unit Testing](#71-unit-testing)
    7.2 [Integration Testing](#72-integration-testing)
    7.3 [System Testing](#73-system-testing)
8. [Appendix](#8-appendix)
    8.1 [Glossary](#81-glossary)

---

## 1. Introduction

### 1.1 Purpose
The purpose of this Software Requirements Specification (SRS) document is to provide a comprehensive and detailed description of the "Hand Made" (Aap ki dukaan) e-commerce application. This document details the functional and non-functional requirements, system architecture, database design, and user interactions. It serves as the primary reference for the development team, quality assurance testers, and project stakeholders to ensure that the final product meets the specified needs. This document is intended to be a complete guide for the lifecycle of the project, from development to deployment and maintenance.

### 1.2 Document Conventions
This document follows the IEEE 830-1998 standard for SRS.
- **Bold** text is used for emphasis, headings, and key terms.
- *Italic* text is used for technical terms, variables, or emphasis on specific conditions.
- `Monospace` font is used for code snippets, database fields, and file paths.
- The document is structured hierarchically, with major sections numbered 1, 2, 3, etc., and subsections numbered 1.1, 1.2, etc.

### 1.3 Intended Audience and Reading Suggestions
This document is intended for a diverse audience:
- **Developers**: To understand the specific functional requirements, architectural constraints, and database schema for implementation.
- **Testers**: To derive test cases and verify the system against the specified requirements.
- **Project Managers**: To track progress, manage scope, and ensure timely delivery.
- **Stakeholders/Clients**: To verify that their business needs and requirements are accurately captured.
- **Maintenance Engineers**: To understand the system structure for future updates and bug fixes.

**Reading Suggestion**:
- **Developers** should focus on Sections 3 (System Architecture), 4 (External Interfaces), and 5 (System Features).
- **Stakeholders** should focus on Sections 1 (Introduction) and 2 (Overall Description).
- **Testers** should read the entire document, with special attention to Section 5 (System Features) and 6 (Nonfunctional Requirements).

### 1.4 Product Scope
"Hand Made" is a specialized web-based e-commerce platform designed to facilitate the sale of unique, handcrafted items. Unlike generic e-commerce sites, "Hand Made" focuses on the aesthetic and narrative value of artisan products such as custom keychains, resin frames, gift hampers, pottery, and wall decor.

**Key Objectives:**
- To provide a visually appealing platform that highlights the craftsmanship of products.
- To offer a seamless and secure shopping experience for customers.
- To provide a robust backend for administrators to manage inventory and orders.
- To implement a responsive design that works across desktops, tablets, and mobile devices.

**Benefits:**
- **For Artisans**: A dedicated platform to showcase and sell their work to a broader audience.
- **For Customers**: Access to unique, high-quality handmade gifts that are not available in mass markets.
- **For Business**: A scalable platform that can grow with the inventory and user base.

### 1.5 References
1.  **Django Documentation**: Official documentation for the Django web framework. [https://docs.djangoproject.com/](https://docs.djangoproject.com/)
2.  **Python Documentation**: Official documentation for the Python programming language. [https://docs.python.org/3/](https://docs.python.org/3/)
3.  **IEEE Std 830-1998**: IEEE Recommended Practice for Software Requirements Specifications.
4.  **MDN Web Docs**: Resources for HTML, CSS, and JavaScript. [https://developer.mozilla.org/](https://developer.mozilla.org/)

## 2. Overall Description

### 2.1 Product Perspective
"Hand Made" is a standalone, self-contained web application. It is built using the Model-View-Template (MVT) architectural pattern provided by the Django framework. It interacts with a relational database to store user and product data and serves dynamic HTML content to the client browser.

**System Interfaces:**
- **Frontend**: The client-side interface is built using HTML5, Vanilla CSS (with a custom premium design system), and JavaScript. It communicates with the backend via HTTP/HTTPS requests.
- **Backend**: The server-side logic is implemented in Python using Django. It handles URL routing, business logic, database interactions, and template rendering.
- **Database**: The system uses SQLite for development and testing, with the capability to migrate to PostgreSQL or MySQL for production environments.
- **Web Server**: The application runs on the Django development server for testing and can be deployed on Gunicorn or uWSGI behind Nginx/Apache for production.

### 2.2 Product Functions
The major functions of the system are categorized as follows:

**User Functions:**
- **Registration**: Users can create a new account by providing their name, email, and password.
- **Login/Logout**: Secure authentication using email/username and password.
- **Browse Catalog**: Users can view a list of all available products.
- **Filter Products**: Users can filter products by category (e.g., Keychains, Frames) and price range.
- **Search**: Users can search for products by name or description.
- **View Product Details**: Users can view detailed information, images, price, and stock status of a specific product.
- **Manage Cart**: Users can add items to their cart, update quantities, and remove items. The cart persists across sessions for logged-in users.
- **Checkout**: Users can proceed to a checkout page (simulated) to finalize their purchase.
- **View Dashboard**: Users can view their profile information and order history.

**Admin Functions:**
- **Manage Products**: Add, edit, and delete products, including uploading images and setting prices/stock.
- **Manage Categories**: Create and manage product categories.
- **Manage Users**: View and manage user accounts.
- **View Orders**: (Future Scope) View and process customer orders.

### 2.3 User Classes and Characteristics
The system identifies three primary user classes:

1.  **Guest User**:
    -   **Characteristics**: Anonymous users who have not logged in.
    -   **Privileges**: Can browse products, search, view details, and add items to a session-based cart. Cannot access the dashboard or complete a purchase without registering/logging in.
    -   **Technical Skill**: Low to Medium.

2.  **Registered User (Customer)**:
    -   **Characteristics**: Users who have created an account and logged in.
    -   **Privileges**: All Guest privileges plus access to the dashboard, persistent cart, and checkout functionality.
    -   **Technical Skill**: Low to Medium.

3.  **Administrator (Superuser)**:
    -   **Characteristics**: System owners or managers with elevated privileges.
    -   **Privileges**: Full access to the Django Admin panel to manage all aspects of the system (users, products, categories, database).
    -   **Technical Skill**: Medium to High.

### 2.4 Operating Environment
-   **Client Side**:
    -   **Device**: Desktop, Laptop, Tablet, Smartphone.
    -   **OS**: Windows, macOS, Linux, Android, iOS.
    -   **Browser**: Chrome, Firefox, Safari, Edge (latest versions recommended).
-   **Server Side**:
    -   **OS**: Linux (Ubuntu/Debian recommended), Windows Server.
    -   **Runtime**: Python 3.8 or higher.
    -   **Framework**: Django 5.0+.
    -   **Database**: SQLite (Dev), PostgreSQL (Prod).

### 2.5 Design and Implementation Constraints
-   **Language**: The backend must be written in Python.
-   **Framework**: The web framework must be Django.
-   **Styling**: The frontend must use Vanilla CSS with a specific "Premium Modern" design aesthetic (Glassmorphism, Gradients). No external CSS frameworks like Bootstrap or Tailwind are to be used to ensure a unique look and lightweight footprint.
-   **Security**: Passwords must never be stored in plain text. Django's built-in authentication system must be used.
-   **Responsiveness**: The site must be fully responsive and functional on mobile devices.

### 2.6 User Documentation
-   **Inline Help**: Tooltips and placeholder text in forms to guide users.
-   **Walkthrough**: A technical walkthrough document (`walkthrough.md`) is provided for developers and maintainers.
-   **README**: A `README.md` file provides setup and installation instructions.

### 2.7 Assumptions and Dependencies
-   **Internet Connection**: Users are assumed to have a stable internet connection.
-   **Browser Support**: Users are assumed to be using a modern web browser that supports HTML5 and CSS3.
-   **Image Assets**: High-quality product images are assumed to be provided by the content team.
-   **Payment Gateway**: For the current version, payment processing is simulated. Integration with a real payment gateway (e.g., Stripe, Razorpay) is a dependency for the final production release.

## 3. System Architecture

### 3.1 Architectural Design
The system follows the **Model-View-Template (MVT)** architecture, which is the standard pattern for Django applications.

-   **Model (Data Layer)**: Defines the logical structure of the database. It handles data storage, retrieval, and validation. Key models include `User`, `Product`, `Category`, `Cart`, and `CartItem`.
-   **View (Business Logic Layer)**: Handles the application logic. It receives HTTP requests, processes them (e.g., fetching data from models), and returns HTTP responses (usually by rendering templates).
-   **Template (Presentation Layer)**: Defines the user interface. It consists of HTML files with Django Template Language (DTL) tags to display dynamic data.

### 3.2 Module Decomposition
The system is decomposed into the following logical modules:

1.  **Authentication Module**: Handles user registration, login, logout, and password management.
2.  **Catalog Module**: Handles product listing, categorization, detail views, and searching.
3.  **Cart Module**: Handles shopping cart operations (add, remove, update, calculate total).
4.  **Dashboard Module**: Handles user profile display and order history.
5.  **Admin Module**: Provides the backend interface for site management.

### 3.3 Database Design
The database schema consists of the following tables:

1.  **auth_user** (Django Built-in):
    -   `id` (PK), `username`, `password`, `email`, `first_name`, `last_name`, `is_staff`, `is_superuser`, `date_joined`.
2.  **hand_made_category**:
    -   `id` (PK), `name` (Char), `slug` (Slug, Unique), `image` (Image).
3.  **hand_made_product**:
    -   `id` (PK), `name` (Char), `slug` (Slug, Unique), `description` (Text), `price` (Decimal), `image` (Image), `stock` (Int), `available` (Bool), `category_id` (FK to Category), `created_at` (DateTime), `updated_at` (DateTime).
4.  **hand_made_cart**:
    -   `id` (PK), `user_id` (OneToOne to User, Nullable), `session_id` (Char, Nullable), `created_at` (DateTime).
5.  **hand_made_cartitem**:
    -   `id` (PK), `cart_id` (FK to Cart), `product_id` (FK to Product), `quantity` (Int).

## 4. External Interface Requirements

### 4.1 User Interfaces
The user interface is designed to be visually striking and user-friendly.

-   **Global Elements**:
    -   **Navbar**: Sticky glassmorphism header with Logo, Navigation Links (Home, Shop, About, Contact), Cart Icon with badge, and User Profile/Login button.
    -   **Footer**: Premium dark gradient footer with Quick Links, Contact Info, Social Media icons, and Copyright.
-   **Home Page**:
    -   **Hero Section**: Full-width animated gradient background with a call-to-action button.
    -   **Featured Products**: Grid layout displaying top products.
    -   **Why Choose Us**: Informational section with icons.
-   **Shop Page**:
    -   **Sidebar**: Accordion-style category filter and price range slider.
    -   **Product Grid**: Responsive grid of product cards with hover effects (Quick View, Add to Cart).
-   **Product Detail Page**:
    -   **Layout**: Split layout with large product image on the left and details on the right.
    -   **Elements**: Product Title, Price, Stock Status, Description, Add to Cart button, Wishlist button.
-   **Cart Page**:
    -   **Desktop**: Table view with columns for Product, Price, Quantity, Total, and Remove action.
    -   **Mobile**: Card-based view for each cart item.
    -   **Summary**: Total calculation and Checkout button.

### 4.2 Hardware Interfaces
The system requires no specific hardware interfaces on the client side other than standard input devices (mouse, keyboard, touch screen). On the server side, it requires a standard server configuration with storage for the database and media files.

### 4.3 Software Interfaces
-   **Django ORM**: Used for all database interactions, abstracting the underlying SQL.
-   **Pillow**: Used for image processing and handling product uploads.
-   **SQLite**: Default database engine.

### 4.4 Communications Interfaces
-   **HTTP/HTTPS**: The primary protocol for client-server communication.
-   **SMTP**: (Optional) For sending email notifications (e.g., welcome emails, password resets).

## 5. System Features (Functional Requirements)

### 5.1 User Authentication Module
**Use Case: User Registration**
-   **Input**: Name, Email, Password, Confirm Password.
-   **Processing**: Validate email format, check if email exists, check password match, hash password, create User record.
-   **Output**: Success message, redirect to Login page.
-   **Error Handling**: Display errors for invalid email, weak password, or existing user.

**Use Case: User Login**
-   **Input**: Username/Email, Password.
-   **Processing**: Authenticate credentials against the database.
-   **Output**: Create session, redirect to Dashboard/Home.
-   **Error Handling**: "Invalid credentials" message.

### 5.2 Product Management Module
**Use Case: View Product List**
-   **Input**: Category filter (optional), Search term (optional).
-   **Processing**: Retrieve products from `hand_made_product` table, apply filters.
-   **Output**: JSON/Context data containing list of products.

**Use Case: View Product Detail**
-   **Input**: Product Slug.
-   **Processing**: Retrieve single product record matching the slug.
-   **Output**: Product object with all details.

### 5.3 Shopping Cart Module
**Use Case: Add to Cart**
-   **Input**: Product ID, Quantity (default 1).
-   **Processing**: Check if Cart exists for user/session. If not, create one. Check if Item exists in Cart. If yes, increment quantity. If no, create CartItem.
-   **Output**: Success message, update Cart badge count.

**Use Case: Remove from Cart**
-   **Input**: CartItem ID.
-   **Processing**: Delete the CartItem record.
-   **Output**: Updated Cart view, recalculated total.

### 5.4 Search and Filtering Module
**Use Case: Search Products**
-   **Input**: Search query string.
-   **Processing**: Perform case-insensitive `icontains` query on Product name and description fields.
-   **Output**: List of matching products.

### 5.5 User Dashboard Module
**Use Case: View Dashboard**
-   **Input**: User ID (from session).
-   **Processing**: Retrieve User details.
-   **Output**: Render dashboard template with user data.

## 6. Other Nonfunctional Requirements

### 6.1 Performance Requirements
-   **Response Time**: 95% of requests should be served within 2 seconds.
-   **Throughput**: The system should support at least 50 concurrent users in the development environment.
-   **Database**: Queries should be optimized using Django's `select_related` and `prefetch_related` to avoid N+1 problems.

### 6.2 Safety Requirements
-   **Data Integrity**: Transactions should be used for critical operations (e.g., checkout) to ensure data consistency.
-   **Backup**: Regular database backups (SQLite file backup) should be performed.

### 6.3 Security Requirements
-   **Authentication**: All administrative functions must require superuser authentication.
-   **Password Storage**: Passwords must be stored using PBKDF2 algorithm with SHA256 hash.
-   **CSRF Protection**: All POST forms must include the `{% csrf_token %}` tag.
-   **XSS Protection**: Django templates auto-escape variables to prevent Cross-Site Scripting.
-   **SQL Injection**: Use of Django ORM prevents SQL injection attacks.

### 6.4 Software Quality Attributes
-   **Reliability**: The system should run 24/7 with 99.9% uptime.
-   **Availability**: The system should be accessible from any location with internet access.
-   **Maintainability**: The code should follow PEP 8 style guidelines and be modular.
-   **Portability**: The application should be easily deployable to different environments (Dev, Staging, Prod) using environment variables.

### 6.5 Business Rules
-   **Pricing**: Prices must be non-negative.
-   **Stock**: Products with 0 stock must be marked as "Out of Stock" and cannot be added to the cart.
-   **Currency**: All transactions are processed in Indian Rupees (₹).

## 7. Testing Strategy

### 7.1 Unit Testing
-   Test individual models (User, Product, Cart) to ensure data integrity and method correctness.
-   Test utility functions and form validations.

### 7.2 Integration Testing
-   Test the interaction between Views and Models.
-   Test the interaction between the Cart module and Product module (e.g., adding a product to cart reduces stock - if implemented).
-   Test URL routing to ensure correct views are called.

### 7.3 System Testing
-   **Functional Testing**: Verify all use cases (Registration, Login, Shopping Flow).
-   **UI/UX Testing**: Verify responsiveness on mobile and desktop, check for broken links and layout issues.
-   **Compatibility Testing**: Test on Chrome, Firefox, and Edge.

## 8. Appendix

### 8.1 Glossary
-   **SRS**: Software Requirements Specification.
-   **MVT**: Model-View-Template (Django's architecture).
-   **ORM**: Object-Relational Mapping.
-   **CSRF**: Cross-Site Request Forgery.
-   **XSS**: Cross-Site Scripting.
-   **Slug**: A URL-friendly version of a string (e.g., "My Product" -> "my-product").
-   **PK**: Primary Key.
-   **FK**: Foreign Key.

---
*End of Document*
