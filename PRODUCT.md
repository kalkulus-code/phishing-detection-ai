# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Delegated: Flask with HTML, CSS, and JavaScript, selected to serve the existing Python model without a separate frontend build.

## Users

Students and lecturers reviewing or demonstrating this phishing email classifier.

## Product Purpose

Let a person submit an email subject and body to the project's trained model and inspect its phishing or safe classification alongside its phishing probability and URL signals. Success means the existing model can be tried through a clear interface and the result is presented without claiming that the classifier's signals explain its decision.

## Positioning

The project uses its checked-in scikit-learn pipeline and URL feature extractor to classify submitted email text locally in the app, rather than sending each email to a third-party analysis API.

## Operating Context

The app is run locally for coursework or a project demonstration. The operator pastes an email subject and body into the interface and requests one analysis.

## Capabilities and Constraints

- The repository includes a trained `model_phishing.pkl` pipeline with TF-IDF text features, URL features, and a Random Forest classifier.
- The model's labels are `0` (safe) and `1` (phishing), according to the training script.
- `feature_extractor.py` extracts URL counts and simple URL traits. These are observable features, not a faithful explanation of the Random Forest's decision.
- The data preparation script expects a CEAS_08 source file that is not included; a prepared training CSV and a trained model are included.
- No original UI, brand identity, or accessibility standard was supplied. The model's training quality and real-world detection performance have not been independently validated.
- Assumption from the user's language and audience: Indonesian is the interface language.

## Evidence on Hand

- `model_phishing.pkl`: the trained model artifact.
- `feature_extractor.py` and `2_train_model.py`: the URL feature extraction and training/evaluation implementation.
- `data_siap_latih.csv`: prepared training data. It is not proof of current model performance.
- No original interface or README was present when this context was recorded.

## Product Principles

- Preserve and call the checked-in model rather than presenting a mock classifier.
- Distinguish the model's predicted label and phishing probability from descriptive URL signals.
- Keep email content within the local app workflow and avoid adding an external analysis service.
- Make the classifier's scope and unknown performance limits clear in the demonstration.
