// // document.addEventListener("DOMContentLoaded", () => {
// //     const symptoms = [
// //         "Feeling nervous", "Panic attacks", "Breathing rapidly", "Sweating",
// //         "Trouble concentrating", "Trouble sleeping", "Trouble with work",
// //         "Hopelessness", "Anger", "Overreacting", "Change in eating habits",
// //         "Suicidal thoughts", "Feeling tired", "No close friends",
// //         "Social media addiction", "Weight gain", "Obsession with material possessions",
// //         "Introversion", "Stressful memories popping up", "Nightmares",
// //         "Avoiding people or activities", "Feeling negative", "Blaming yourself",
// //     ];

// //     const questionsContainer = document.getElementById("questions-container");

// //     symptoms.forEach((symptom, index) => {
// //         const questionContainer = document.createElement("div");
// //         questionContainer.classList.add("question-box");
// //         questionContainer.innerHTML = `
// //             <label>${symptom}?</label>
// //             <div>
// //                 <input type="radio" name="symptom-${index}" value="1" required> Yes
// //                 <input type="radio" name="symptom-${index}" value="0" required> No
// //             </div>
// //         `;
// //         questionsContainer.appendChild(questionContainer);
// //     });

// //     document.getElementById("symptom-form").addEventListener("submit", async (event) => {
// //         event.preventDefault();

// //         // Collect form data
// //         const formData = new FormData(event.target);
// //         const symptoms = Array.from(formData.values()).map(value => parseInt(value, 10));

// //         // Validasi jumlah input
// //         if (symptoms.length !== 24) {  // Pastikan sesuai jumlah pertanyaan
// //             alert("Please answer all questions before submitting!");
// //             return;
// //         }

// //         try {
// //             const response = await fetch("http://127.0.0.1:8000/api/predict", {
// //                 method: "POST",
// //                 headers: {
// //                     "Content-Type": "application/json",
// //                 },
// //                 body: JSON.stringify({ symptoms }),
// //             });

// //             const result = await response.json();
// //             if (response.ok) {
// //                 alert(`Your mental health prediction: ${result.prediction}`);
// //             } else {
// //                 alert(`Error: ${result.detail}`);
// //             }
// //         } catch (error) {
// //             console.error("Error:", error);
// //             alert("Failed to submit data. Please try again.");
// //         }
// //     });
// // });

// document.addEventListener("DOMContentLoaded", () => {
//     const symptoms = [
//         "Feeling nervous", "Panic attacks", "Breathing rapidly", "Sweating",
//         "Trouble concentrating", "Trouble sleeping", "Trouble with work",
//         "Hopelessness", "Anger", "Overreacting", "Change in eating habits",
//         "Suicidal thoughts", "Feeling tired", "No close friends",
//         "Social media addiction", "Weight gain", "Obsession with material possessions",
//         "Introversion", "Stressful memories popping up", "Nightmares",
//         "Avoiding people or activities", "Feeling negative", "Blaming yourself",
//     ];

//     const questionsContainer = document.getElementById("questions-container");

//     symptoms.forEach((symptom, index) => {
//         const questionContainer = document.createElement("div");
//         questionContainer.classList.add("question-box");
//         questionContainer.innerHTML = `
//             <label>${symptom}?</label>
//             <div>
//                 <input type="radio" name="symptom-${index}" value="1" required> Yes
//                 <input type="radio" name="symptom-${index}" value="0" required> No
//             </div>
//         `;
//         questionsContainer.appendChild(questionContainer);
//     });

//     document.getElementById("symptom-form").addEventListener("submit", async (event) => {
//         event.preventDefault();

//         // Collect form data
//         const formData = new FormData(event.target);
//         const symptoms = Array.from(formData.values()).map(value => parseInt(value, 10));

//         // Validasi jumlah input
//         if (symptoms.length !== 24) {  // Pastikan sesuai jumlah pertanyaan
//             alert("Please answer all questions before submitting!");
//             return;
//         }

//         try {
//             const response = await fetch("http://127.0.0.1:8000/api/predict", {
//                 method: "POST",
//                 headers: {
//                     "Content-Type": "application/json",
//                 },
//                 body: JSON.stringify({ symptoms }),
//             });

//             const result = await response.json();
//             if (response.ok) {
//                 alert(`Your mental health prediction: ${result.prediction}`);
//             } else {
//                 alert(`Error: ${result.detail}`);
//             }
//         } catch (error) {
//             console.error("Error:", error);
//             alert("Failed to submit data. Please try again.");
//         }
//     });
// });

document.addEventListener("DOMContentLoaded", () => {
    const symptoms = [
        "Feeling nervous", "Panic attacks", "Breathing rapidly", "Sweating",
        "Trouble concentrating", "Trouble sleeping", "Trouble with work",
        "Hopelessness", "Anger", "Overreacting", "Change in eating",
        "Suicidal thoughts", "Feeling tired", "No close friends",
        "Social media addiction", "Weight gain", "Material possessions",
        "Introvert", "Stressful memories", "Nightmares",
        "Avoiding people or activities", "Trouble concentrating", "Feeling negative", "Blaming yourself",
    ];

    const questionsContainer = document.getElementById("questions-container");

    // Generate questions dynamically
    symptoms.forEach((symptom, index) => {
        const questionContainer = document.createElement("div");
        questionContainer.classList.add("question-box");
        questionContainer.innerHTML = `
            <label>${symptom}?</label>
            <div>
                <input type="radio" name="symptom-${index}" value="1" required> Yes
                <input type="radio" name="symptom-${index}" value="0" required> No
            </div>
        `;
        questionsContainer.appendChild(questionContainer);
    });

    document.getElementById("symptom-form").addEventListener("submit", async (event) => {
        event.preventDefault();

        // Collect form data
        const formData = new FormData(event.target);
        const symptoms = Array.from(formData.values()).map(value => parseInt(value, 10));

        // Validasi jumlah input
        if (symptoms.length !== symptoms.length) {  // Memastikan jumlah input sesuai jumlah pertanyaan
            alert("Please answer all questions before submitting!");
            return;
        }

        try {
            const response = await fetch("http://127.0.0.1:8000/api/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ symptoms }),
            });

            const result = await response.json();
            if (response.ok) {
                alert(`Your mental health prediction: ${result.prediction}`);
            } else {
                alert(`Error: ${result.detail}`);
            }
        } catch (error) {
            console.error("Error:", error);
            alert("Failed to submit data. Please try again.");
        }
    });
});
