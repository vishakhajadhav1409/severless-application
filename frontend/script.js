// AWS SAM Local API URL
const API_URL = "http://127.0.0.1:3000/students";

document.getElementById("studentForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;

    const studentData = {
        name: name,
        email: email
    };

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(studentData)
        });

        const result = await response.json();

        if (response.ok) {
            document.getElementById("message").innerHTML =
                "✅ Student Registered Successfully!";

            document.getElementById("studentForm").reset();
        } else {
            document.getElementById("message").innerHTML =
                "❌ Error: " + result.message;
        }

    } catch (error) {
        console.error("Error:", error);

        document.getElementById("message").innerHTML =
            "❌ Unable to connect with server";
    }
});