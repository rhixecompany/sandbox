<<<<<<< HEAD
import React from "react";
import {
  Edit,
  SimpleForm,
  TextInput,
  ImageInput,
  DateInput,
} from "react-admin";

const SeriesEdit = (props) => {
  return (
    <Edit title="Edit Movie" {...props}>
      <SimpleForm>
        <TextInput disabled source="_id" />
        <TextInput source="name" />
        <ImageInput label="Image" source="image" />
        <DateInput label="Date" source="updateAt" />
      </SimpleForm>
    </Edit>
  );
};

export default SeriesEdit;
=======
import React from "react";
import {
  Edit,
  SimpleForm,
  TextInput,
  ImageInput,
  DateInput,
} from "react-admin";

const SeriesEdit = (props) => {
  return (
    <Edit title="Edit Movie" {...props}>
      <SimpleForm>
        <TextInput disabled source="_id" />
        <TextInput source="name" />
        <ImageInput label="Image" source="image" />
        <DateInput label="Date" source="updateAt" />
      </SimpleForm>
    </Edit>
  );
};

export default SeriesEdit;
>>>>>>> 6031d8f (chore: initial local project setup for xamehi.tv)
