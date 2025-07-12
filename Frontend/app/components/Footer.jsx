
export default function Footer() {
  return (
    <footer className="footer">
      <p className="fade-in">
        &copy; {new Date().getFullYear()} <strong>Disease Predictor</strong>. All rights reserved.
      </p>
    </footer>
  );
}
