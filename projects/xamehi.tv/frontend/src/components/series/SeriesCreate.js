import React from "react";
import {
  Create,
  SimpleForm,
  TextInput,
  ImageInput,
  DateInput,
} from "react-admin";

const SeriesCreate = (props) => {
  return (
    <Create title="Create a Movie" {...props}>
      <SimpleForm>
        <TextInput source="_id" />
        <TextInput source="name" />
        <ImageInput source="image" />
        <DateInput label="Date" source="updateAt" />
      </SimpleForm>
    </Create>
  );
};

export default SeriesCreate;
import React from "react";
import {
  Create,
  SimpleForm,
  TextInput,
  ImageInput,
  DateInput,
} from "react-admin";

const SeriesCreate = (props) => {
  return (
    <Create title="Create a Movie" {...props}>
      <SimpleForm>
        <TextInput source="_id" />
        <TextInput source="name" />
        <ImageInput source="image" />
        <DateInput label="Date" source="updateAt" />
      </SimpleForm>
    </Create>
  );
};

export default SeriesCreate;
