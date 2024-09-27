document.addEventListener('DOMContentLoaded', function() {
    const categorySelect = document.getElementById('id_category');
    const subjectSelect = document.getElementById('id_subject');

    categorySelect.addEventListener('change', function() {
        const categoryId = this.value;

        fetch(`/chapters/filter-subjects/?category_id=${categoryId}`, {
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => response.json())
        .then(data => {
            subjectSelect.innerHTML = ''; // Clear current options
            data.forEach(subject => {
                const option = document.createElement('option');
                option.value = subject.id;
                option.textContent = subject.subject_name;
                subjectSelect.appendChild(option);
            });
        })
        .catch(error => console.error('Error fetching subjects:', error));
    });
});
