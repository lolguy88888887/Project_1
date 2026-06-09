```javascript
document.getElementById("careerForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const math = document.getElementById("math").value;
    const coding = document.getElementById("coding").value;
    const art = document.getElementById("art").value;
    const social = document.getElementById("social").value;
    const science = document.getElementById("science").value;

    // TEMPORARY fake prediction
    // Replace this later with your Python backend

    let career = "Unknown";

    if (coding > 7 && math > 7) {
        career = "Software Engineer";
    } else if (art > 7) {
        career = "Designer";
    } else if (science > 7) {
        career = "Doctor";
    } else {
        career = "Teacher";
    }

    document.getElementById("result").innerHTML =
        "Predicted Career: " + career;
});
```
