document.getElementById("salaryForm").addEventListener("submit", async function(e){

    e.preventDefault();

    const data = {
        company: company.value,
        department: department.value,
        age: Number(age.value),
        age_when_joined: Number(age_when_joined.value),
        years_in_the_company: Number(years_in_the_company.value),
        annual_bonus: Number(annual_bonus.value),
        prior_years_experience: Number(prior_years_experience.value),
        full_time: Number(full_time.value),
        part_time: Number(part_time.value),
        contractor: Number(contractor.value),
        age_diff: Number(age_diff.value),
        bonus_per_year: Number(bonus_per_year.value),
        total_experience: Number(total_experience.value),
        experience_ratio: Number(experience_ratio.value),
        company_department: company_department.value,
        employment_type: employment_type.value
    };

    const response = await fetch("/predict",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify(data)
    });

    const result = await response.json();

    document.getElementById("result").innerHTML =
        "Predicted Salary: ₹ " + result.predicted_salary;
});