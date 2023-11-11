-- https://leetcode.com/problems/combine-two-tables/?lang=pythondata

-- Write your PostgreSQL query statement below
SELECT p.firstName, p.lastName, a.city, a.state from person p LEFT JOIN address a ON p.personId = a.personId;
