# Smart Waste AI ♻️

## AI-Based Smart Waste Segregation Assistant

Smart Waste AI is a simple AI-assisted web application that helps users identify the appropriate waste category for common household waste items and provides disposal guidance and sustainability tips.

This project was developed as part of the **1M1B AI for Sustainability Virtual Internship** and is aligned with **UN Sustainable Development Goal 12 – Responsible Consumption and Production**.

---

## 🎯 Problem Statement

Improper waste segregation can lead to environmental pollution, inefficient recycling, and unsafe disposal of hazardous and electronic waste.

Many people are unsure about which category a waste item belongs to or how it should be disposed of.

Smart Waste AI addresses this problem by providing a simple interface where users can enter a waste item and receive a suggested waste category, disposal guidance, and a sustainability tip.

---

## 💡 Solution

The application classifies waste items into five categories:

- 🟢 Wet / Organic Waste
- 🔵 Dry / Recyclable Waste
- 🔴 Hazardous Waste
- 🟣 E-Waste
- ⚪ Unknown

The system provides:

- Waste category
- Disposal guidance
- Sustainability tip
- Confidence indication for classification

---

## 🤖 AI Elements

The project uses AI-assisted development and intelligent text matching to improve waste classification.

### AI-related components

- AI-assisted coding and development using **IBM Bob**
- Keyword-based waste classification
- Fuzzy text matching using **RapidFuzz**
- Input matching for common spelling variations and similar terms

RapidFuzz helps the application recognize inputs that may not exactly match the stored waste-item names.

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML
- CSS
- RapidFuzz
- GitHub
- IBM Bob

---

## 🌍 SDG Alignment

### UN SDG 12 – Responsible Consumption and Production

Smart Waste AI supports responsible waste management by helping users understand waste categories and encouraging proper segregation and disposal.

The project aims to promote:

- Better waste segregation
- Recycling awareness
- Responsible disposal
- Reduction of improper waste handling
- Environmental awareness

---

## ⚙️ How It Works

```text
User enters waste item
        ↓
Input is processed
        ↓
Waste item is matched
        ↓
Waste category is identified
        ↓
Disposal guidance is displayed
        ↓
Sustainability tip is provided
