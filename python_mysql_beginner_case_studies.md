# Python & MySQL Beginner Case Studies: Single-Table Practice Projects

## Overview & Purpose
This collection contains four beginner-friendly backend practice case studies designed for learning **Python** and **MySQL** database integration using `mysql-connector-python`. 

Each project models a real-world software system centered around a **single, flat database table** (no complex foreign keys or multi-table joins required). These exercises help beginners master:
1. **CRUD Operations** (Create, Read, Update, Delete)
2. **Filtering & Searching** (`WHERE`, `LIKE`)
3. **Data Aggregations & Statistics** (`COUNT`, `SUM`, `AVG`, `GROUP BY`)
4. **Input Validation & Business Logic**
5. **Future AI Integration Concepts** (LLM Prompts, RAG, Agents with LangChain/Gemini)

---


### 2. Technology Stack
- **Language:** Python 3.x
- **Database:** MySQL
- **Driver:** `mysql-connector-python`

*Future Extensions:* Django, Django REST Framework, Gemini API, Pydantic, LangChain.

---

### 3. Database Schema

```sql
CREATE DATABASE inventory_db;

USE inventory_db;

CREATE TABLE inventory (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    sku VARCHAR(50) UNIQUE NOT NULL,
    category VARCHAR(50) NOT NULL,
    quantity INT DEFAULT 0,
    reorder_level INT DEFAULT 10,
    unit_price DECIMAL(10, 2) DEFAULT 0.00,
    storage_zone VARCHAR(20) DEFAULT 'Zone-A',
    status VARCHAR(20) DEFAULT 'In Stock',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Task 2: Hospital Patient Register

### Project Abstract
Build a **Hospital Patient Register** using **Python and MySQL**.

The purpose of this project is to learn basic database interactions using a single table to manage patient entries, doctor assignments, appointment statuses, and billing amounts.

Clinic staff can register new patients, view active visits, update treatment statuses, and compute daily clinic revenue.

---

### 1. Real-World Scenario
Imagine a small outpatient clinic.

A receptionist encounters a quick operational task:
> *"Patient John Doe is calling to check his appointment status with Dr. Sarah for today and needs to update his phone number."*

The reception team should be able to:
- Register a new patient visit record
- View all registered patient visits
- Search for a patient by phone number or name
- Update appointment status (`Pending`, `Completed`, `Cancelled`) or assigned doctor
- Delete duplicate or erroneous patient entries
- Filter patients by status or department
- Calculate total consultation fees collected
- Count total appointments per doctor

Later, AI can automatically analyze these logs to determine:
- Summary of patient complaints for doctor quick-review
- Automated follow-up reminder messages
- Priority tagging based on symptom description

---

### 2. Technology Stack
- **Language:** Python 3.x
- **Database:** MySQL
- **Driver:** `mysql-connector-python`

*Future Extensions:* Django, Django REST Framework, Gemini API, Pydantic, LangChain.

---

### 3. Database Schema

```sql
CREATE DATABASE hospital_db;

USE hospital_db;

CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    assigned_doctor VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    appointment_date DATE NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending',
    consultation_fee DECIMAL(10, 2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Task 3: Automobile Service Job Tracker

### Project Abstract
Build an **Automobile Service Job Tracker** using **Python and MySQL**.

The purpose of this project is to manage auto workshop repair jobs inside a single database table, tracking customer details, vehicle complaints, assigned mechanics, and repair costs.

Workshop advisors can create job cards, track job progression, update final billing, and analyze overall workshop revenue.

---

### 1. Real-World Scenario
Imagine a local auto repair shop.

A service advisor encounters a routine task:
> *"A customer brought in a Honda Civic reporting a screeching brake noise. The advisor needs to log the job, set the status to 'In Repair', assign mechanic Alex, and enter the estimated cost."*

The workshop team should be able to:
- Create a new repair job entry
- View all active job cards
- Search for job cards by vehicle license plate number or customer name
- Update repair status (`Received`, `In Repair`, `Ready for Pickup`, `Delivered`)
- Update final bill amount when work is finished
- Delete cancelled or invalid job entries
- Filter jobs by current repair status or assigned mechanic
- Calculate total revenue earned from completed jobs

Later, AI can automatically analyze job logs to determine:
- Estimated repair time based on reported vehicle issues
- Auto-generated service summary to send to customers via SMS/Email
- Preliminary diagnostic suggestions based on reported symptoms

---

### 2. Technology Stack
- **Language:** Python 3.x
- **Database:** MySQL
- **Driver:** `mysql-connector-python`

*Future Extensions:* Django, Django REST Framework, Gemini API, Pydantic, LangChain.

---

### 3. Database Schema

```sql
CREATE DATABASE auto_service_db;

USE auto_service_db;

CREATE TABLE job_cards (
    job_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    vehicle_number VARCHAR(20) NOT NULL,
    vehicle_model VARCHAR(50) NOT NULL,
    issue_description TEXT NOT NULL,
    assigned_mechanic VARCHAR(100) DEFAULT 'Unassigned',
    status VARCHAR(30) DEFAULT 'Received',
    estimated_cost DECIMAL(10, 2) DEFAULT 0.00,
    final_bill DECIMAL(10, 2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Task 4: Hotel Room Booking Manager

### Project Abstract
Build a **Hotel Room Booking Manager** using **Python and MySQL**.

The purpose of this project is to handle hotel stay reservations in a single table, tracking guest details, stay dates, room types, payment statuses, and booking amounts.

Front-desk staff can add new reservations, check room statuses, update stay dates, and track overall hotel revenue.

---

### 1. Real-World Scenario
Imagine a boutique hotel during peak season.

A front-desk manager encounters a guest request:
> *"A guest wants to check into Room 204 for 3 nights in a Deluxe category. The manager needs to record the booking, confirm payment status, and mark the status as 'Checked-In'."*

The hotel staff should be able to:
- Add a new booking entry with room and guest details
- View all current bookings
- Search bookings by guest name or room number
- Update booking status (`Reserved`, `Checked-In`, `Checked-Out`, `Cancelled`)
- Update total payment amount upon check-out
- Delete cancelled or mistaken reservations
- Filter bookings by room category or status
- Calculate total revenue collected across all completed stays

Later, AI can automatically analyze booking records to determine:
- Dynamic price suggestions based on high room demand
- Personalized welcome messages for guests
- Guest feedback sentiment summaries based on stay logs

---

### 2. Technology Stack
- **Language:** Python 3.x
- **Database:** MySQL
- **Driver:** `mysql-connector-python`

*Future Extensions:* Django, Django REST Framework, Gemini API, Pydantic, LangChain.

---

### 3. Database Schema

```sql
CREATE DATABASE hotel_db;

USE hotel_db;

CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    guest_name VARCHAR(100) NOT NULL,
    room_number VARCHAR(10) NOT NULL,
    room_type VARCHAR(50) NOT NULL,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    status VARCHAR(20) DEFAULT 'Reserved',
    total_amount DECIMAL(10, 2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---
